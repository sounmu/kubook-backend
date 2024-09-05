from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from routes.response.bookrequest_response import BookRequestResponse
from domain.schemas.bookrequest_schemas import DeleteBookRequestRequest
from domain.services.bookrequest_service import delete_bookrequest as service_delete_bookrequest
from dependencies import get_current_active_user, get_db

router = APIRouter(
    prefix="/book-requests",
    tags=["book-requests"],
    dependencies=[Depends(get_current_active_user)]
)


@router.delete(
    "/{request_id}",
    summary="도서 구매 요청 삭제 (요청자 취소)",
    response_model=BookRequestResponse,
    status_code=status.HTTP_200_OK
)
async def delete_my_bookrequests(
    request_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    domain_req = DeleteBookRequestRequest(request_id=request_id, processing_status=2, is_deleted=True)
    domain_res = await service_delete_bookrequest(domain_req, db)
    result = BookRequestResponse(
        user_id=domain_res.user_id,
        request_id=domain_res.request_id,
        book_title=domain_res.book_title,
        publication_year=domain_res.publication_year,
        request_link=domain_res.request_link,
        reason=domain_res.reason,
        processing_status=domain_res.processing_status,
        request_date=domain_res.request_date,
        reject_reason=domain_res.reject_reason
    )
    return result
