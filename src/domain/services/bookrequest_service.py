from datetime import datetime as _datetime

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from domain.schemas.bookrequest_schemas import DomainReqPostBookRequest, DomainResPostBookRequest
from repositories.models import RequestedBook


async def service_create_bookrequest(request: DomainReqPostBookRequest, db: Session):
    # check if the book already exists in database
    stmt = select(RequestedBook).where(RequestedBook.book_title == request.book_title)
    valid_request = db.execute(stmt).scalar_one_or_none()

    if valid_request:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Already requested book")

    purchase_request = RequestedBook(
        user_id=request.user_id,
        book_title=request.book_title,
        publication_year=request.publication_year,
        request_link=request.request_link,
        requested_at=_datetime.now(),
        reason=request.reason,
        processing_status=0
    )

    try:
        db.add(purchase_request)
        db.flush()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f"Integrity Error occurred during create the new {purchase_request} item. {str(e)}")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected error occurred: {str(e)}")
    else:
        db.commit()
        db.refresh(purchase_request)

        result = DomainResPostBookRequest(
            request_id=purchase_request.id,
            user_id=purchase_request.user_id,
            book_title=purchase_request.book_title,
            publication_year=purchase_request.publication_year,
            request_link=purchase_request.request_link,
            requested_at=purchase_request.requested_at,
            reason=purchase_request.reason,
            processing_status=purchase_request.processing_status
        )
        return result
