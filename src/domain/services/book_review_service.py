from fastapi import HTTPException, status
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select, and_

from domain.schemas.book_review_schemas import BookReviewByInfoId
from repositories.models import BookReview, User
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
        .order_by(BookReview.created_at)
    )
    try:
        reviews = db.execute(stmt).scalars().all()  # loans를 리스트로 반환

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

        )

    return response
