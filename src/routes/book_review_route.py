from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session

from dependencies import get_current_active_user, get_db
from routes.response.book_review_response import BookReviewListByInfoIdResponse
from domain.services.book_review_service import get_all_reviews_by_bookinfo_id as service_get_all_reviews_by_bookinfo_id

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
