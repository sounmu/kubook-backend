from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session

from dependencies import get_current_active_user, get_db
from routes.response.book_review_response import BookReviewListResponse, BookReviewListByInfoIdResponse
from domain.schemas.book_review_schemas import BookReviewCreateRequest, BookReviewCreateResponse
from domain.services.book_review_service import get_all_user_reviews as service_get_all_user_reviews
from domain.services.book_review_service import get_all_reviews_by_bookinfo_id as service_get_all_reviews_by_bookinfo_id
from domain.services.book_review_service import delete_review as service_delete_review
from domain.services.book_review_service import create_review as service_create_review

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
    dependencies=[Depends(get_current_active_user)]
)


@router.get(
    "/",
    response_model=BookReviewListByInfoIdResponse,
    status_code=status.HTTP_200_OK,
    summary="책에 대한 리뷰 조회"
)
async def get_all_reviews_by_bookinfo_id(
    book_info_id: int = Query(alias="books"),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    domain_res = await service_get_all_reviews_by_bookinfo_id(book_info_id, db)

    result = BookReviewListByInfoIdResponse(
        data=domain_res,
        count=len(domain_res)
    )

    return result

 @router.get(
    "/{user_id}/reviews",
    response_model=BookReviewListResponse,
    status_code=status.HTTP_200_OK,
    summary="회원의 전체 리뷰 목록 조회",
)
async def get_all_user_reviews(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    domain_res = await service_get_all_user_reviews(current_user.id, db)

    result = BookReviewListResponse(
        data=domain_res,
        count=len(domain_res)
    )
    return result


@router.post(
    "",
    response_model=BookReviewCreateResponse,
    status_code=status.HTTP_200_OK,
    summary="리뷰 작성"
)
async def create_review(
    book_info_id: int,
    review_content: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    domain_req = BookReviewCreateRequest(
        user_id=current_user.id,
        book_info_id=book_info_id,
        review_content=review_content
    )
    result = await service_create_review(domain_req, db)
    return result


@router.delete(
    "/{review_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="리뷰 삭제"
)
async def delete_reivew(
    review_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    await service_delete_review(review_id, current_user.id, db)
    return

