from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dependencies import get_current_active_user, get_db
from domain.schemas.bookrequest_schemas import RouteReqPostBookRequest, RouteResPostBookRequest
from domain.services.bookrequest_service import service_create_bookrequest

router = APIRouter(
    prefix="/book-requests",
    tags=["book-requests"],
    dependencies=[Depends(get_current_active_user)]
)


@router.post(
    "",
    response_model=RouteResPostBookRequest,
    status_code=status.HTTP_200_OK,
    summary="구매 요청"
)
async def create_book_request(
    PurchaseCreate: RouteReqPostBookRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    domain_req = RouteReqPostBookRequest(
        user_id=current_user.id,
        book_title=PurchaseCreate.book_title,
        publication_year=PurchaseCreate.publication_year,
        request_link=PurchaseCreate.request_link,
        reason=PurchaseCreate.reason
    )
    result = await service_create_bookrequest(domain_req, db)
    return result
