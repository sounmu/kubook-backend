from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from dependencies import get_current_active_user, get_db
from domain.schemas.book_review_schemas import (
    DomainReqPostReview,
    DomainReqPutReview,
    DomainResGetReviewItem,
    DomainResPostReview,
)
from domain.services.book_review_service import (
    service_create_review,
    service_delete_review,
    service_read_reviews_by_bookinfo_id,
    service_read_reviews_by_user_id,
    service_update_review,
)
from routes.request.book_review_request import BookReviewUpdateRouteRequest
from routes.response.book_review_response import BookReviewListByInfoIdResponse, BookReviewListResponse

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
    domain_res = await service_read_reviews_by_bookinfo_id(book_info_id, db)

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
    domain_res = await service_read_reviews_by_user_id(current_user.id, db)

    result = BookReviewListResponse(
        data=domain_res,
        count=len(domain_res)
    )
    return result


@router.post(
    "",
    response_model=DomainResPostReview,
    status_code=status.HTTP_200_OK,
    summary="리뷰 작성"
)
async def create_review(
    book_info_id: int,
    review_content: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    domain_req = DomainReqPostReview(
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

@router.put(
    "/{review_id}",
    response_model=DomainResGetReviewItem,
    status_code=status.HTTP_200_OK,
    summary="리뷰 수정"
)
async def update_review(
    review_id: int,
    review_update_data: BookReviewUpdateRouteRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    domain_req = DomainReqPutReview(
        review_id=review_id,
        review_content=review_update_data.review_content,
        user_id=current_user.id
    )
    result = await service_update_review(domain_req, db)
    return result

