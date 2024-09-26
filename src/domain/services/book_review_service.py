
from datetime import datetime as _datetime

from fastapi import HTTPException, status
from sqlalchemy import and_, select
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session, selectinload

from domain.schemas.book_review_schemas import (
    BookReviewByInfoId,
    BookReviewCreateRequest,
    BookReviewCreateResponse,
    BookReviewItem,
    BookReviewUpdateRequest,
)
from repositories.models import BookInfo, BookReview, User
from utils.crud_utils import get_item


async def get_all_reviews_by_bookinfo_id(book_info_id, db: Session):
    stmt = (
        select(BookReview)
        .options(selectinload(BookReview.user))
        .where(
            and_(
                BookReview.book_info_id == book_info_id,
                BookReview.is_deleted == False
            )
        )
        .order_by(BookReview.updated_at)
    )
    try:
        reviews = db.execute(stmt).scalars().all()

        if not reviews:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Reviews not found"
            )

        response = [
            BookReviewByInfoId(
                review_id=review.id,
                user_id=review.user_id,
                user_name=review.user.user_name,
                review_content=review.review_content,
                created_at=review.created_at,
                updated_at=review.updated_at
            )
            for review in reviews
        ]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error occurred during retrieve: {str(e)}"
            ) from e

    return response



async def get_all_user_reviews(user_id, db: Session):
    stmt = (
        select(BookReview)
        .where(
            and_(
                BookReview.user_id == user_id,
                BookReview.is_deleted == False
            )
        )
        .order_by(BookReview.updated_at))

    try:
        reviews = db.scalars(stmt).all()  # loans를 리스트로 반환
        if not reviews:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Reviews not found")

        result = [
            BookReviewItem(
                review_id=review.id,
                user_id=review.user_id,
                book_info_id=review.book_info_id,
                review_content=review.review_content,
                created_at=review.created_at,
                updated_at=review.updated_at
            )
            for review in reviews
        ]

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error occurred during retrieve: {str(e)}"
            ) from e
    return result


async def delete_review(review_id, user_id, db: Session):
    stmt = select(BookReview).where(and_(BookReview.id == review_id, BookReview.is_deleted == False))

    try:
        review = db.execute(stmt).scalar_one()

        if review.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="You do not have permission to access this review.")

        review.is_deleted = True
        review.updated_at = _datetime.now()

        db.flush()

    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Loan not found"
        ) from None
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error occurred during update: {str(e)}"
            ) from e
    else:
        db.commit()
        return


async def create_review(request: BookReviewCreateRequest, db: Session):
    stmt = select(BookInfo).where(BookInfo.id == request.book_info_id)
    valid_book_info = db.execute(stmt).scalar_one_or_none()

    if not valid_book_info:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid book info ID"
            )

    review = BookReview(
        user_id=request.user_id,
        book_info_id=request.book_info_id,
        review_content=request.review_content,
        created_at=_datetime.now(),
        updated_at=_datetime.now()
    )

    try:
        db.add(review)
        db.flush()

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error occurred: {str(e)}"
            ) from e
    else:
        db.commit()
        db.refresh(review)

        user = get_item(User, request.user_id, db)
        result = BookReviewCreateResponse(
            review_id=review.id,
            user_id=review.user_id,
            user_name=user.user_name,
            book_info_id=review.book_info_id,
            review_content=review.review_content,
            created_at=review.created_at,
        )
        return result


async def update_review(request: BookReviewUpdateRequest, db: Session):
    stmt = select(BookReview).where(and_(BookReview.id == request.review_id, BookReview.is_deleted == False))

    try:
        review = db.execute(stmt).scalar_one()

        if review.user_id != request.user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="You do not have permission to access this review.")

        review.review_content = request.review_content
        review.updated_at = _datetime.now()

        db.flush()
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found"
            ) from None
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Integrity Error occurred during update the Review item.: {str(e)}"
            ) from None
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error occurred during update: {str(e)}"
            ) from e
    else:
        db.commit()
        db.refresh(review)

        response = BookReviewItem(
            review_id=review.id,
            user_id=review.user_id,
            book_info_id=review.book_info_id,
            review_content=review.review_content,
            created_at=review.created_at,
            updated_at=review.updated_at
        )

        return response

