from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from dependencies import get_current_active_user, get_db
from domain.schemas.bookrequest_schemas import DomainReqDelBookRequest
from domain.services.bookrequest_service import service_delete_bookrequest

router = APIRouter(
    prefix="/book-requests",
    tags=["book-requests"],
    dependencies=[Depends(get_current_active_user)]
)


@router.delete(
    "/{request_id}",
    summary="도서 구매 요청 삭제 (요청자 취소)",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user_bookrequest (
    request_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user)
) -> None:
    domain_req = DomainReqDelBookRequest(request_id=request_id, processing_status=2)
    await service_delete_bookrequest(domain_req, db)

    return
