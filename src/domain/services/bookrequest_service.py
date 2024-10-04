
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
from utils.crud_utils import delete_item


async def service_update_bookrequest(request_data: DomainReqPutBookRequest, db: Session):
    stmt = (select(RequestedBook).where(
            and_(RequestedBook.id==request_data.request_id,
                 RequestedBook.user_id==request_data.user_id,
                 RequestedBook.is_deleted==False))
            .order_by(RequestedBook.updated_at))
    try:
        item = db.execute(stmt).scalar_one()
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Requested book not found")
        request_book = item.__dict__
        updated_book = request_data.__dict__
        for key, value in updated_book.items():
            if value is not None and key in request_book:
                if isinstance(value, type(request_book[key])):
                    setattr(item, key, value)
                else:
                    raise HTTPException(
                        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        detail=f"Invalid value type for column {key}. Expected {type(request_book[key])}, got {type(value)}."
                    )
        db.add(item)
        db.flush()
    except HTTPException as e:
        db.rollback()
        raise e
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected error occurred during update: {str(e)}") from e
    else:
        db.commit()
        db.refresh(item)
        # domain response schema 생성
        response = DomainResBookRequest(
        user_id=item.user_id,
        request_id=item.id,
        book_title=item.book_title,
        publication_year=item.publication_year,
        request_link=item.request_link,
        reason=item.reason,
            processing_status=item.processing_status,
            request_date=item.requested_at.date(),
            reject_reason=item.reject_reason
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
