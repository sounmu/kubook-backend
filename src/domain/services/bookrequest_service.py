
from fastapi import HTTPException, status
from sqlalchemy import and_, select
from sqlalchemy.orm import Session

from domain.schemas.bookrequest_schemas import (
    DomainReqDelBookRequest,
    DomainReqGetBookRequest,
    DomainReqPutBookRequest,
    DomainResBookRequest,
)
from repositories.models import RequestedBook
from utils.crud_utils import delete_item, update_item


async def service_update_bookrequest(request_data: DomainReqPutBookRequest, db: Session):
    updated_book = update_item(RequestedBook, request_data.request_id, request_data, db)
    # domain response schema 생성
    response = DomainResBookRequest(
        user_id=updated_book.user_id,
        request_id=updated_book.id,
        book_title=updated_book.book_title,
        publication_year=updated_book.publication_year,
        request_link=updated_book.request_link,
        reason=updated_book.reason,
        processing_status=updated_book.processing_status,
        request_date=updated_book.requested_at.date(),
        reject_reason=updated_book.reject_reason
    )
    return response


async def service_read_bookrequest(request_data: DomainReqGetBookRequest, db: Session) -> list[DomainResBookRequest]:
    stmt = (select(RequestedBook).where(and_(RequestedBook.user_id==request_data.user_id, RequestedBook.is_deleted==False))
            .order_by(RequestedBook.updated_at))
    try:
        requested_book_list = db.scalars(stmt).all()
        if not requested_book_list:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Requested book not found")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected error occurred during retrieve: {str(e)}") from e
    response = [DomainResBookRequest(
        request_id=book.id,
        user_id=book.user_id,
        book_title=book.book_title,
        publication_year=book.publication_year,
        request_link=book.request_link,
        reason=book.reason,
        processing_status=book.processing_status,
        request_date=book.requested_at.date(),
        reject_reason=book.reject_reason
        ) for book in requested_book_list]
    return response

async def service_delete_bookrequest(request_data: DomainReqDelBookRequest, db: Session):
    delete_item(RequestedBook, request_data.request_id, db)
    return
