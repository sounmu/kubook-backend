from datetime import datetime as _datetime

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.schemas.bookrequest_schemas import DomainReqPostBookRequest, DomainResPostBookRequest
from repositories.models import RequestedBook, User


async def service_create_bookrequest(request: DomainReqPostBookRequest, db: Session):
    # check if the book already exists in database
    stmt = select(RequestedBook).where(RequestedBook.book_title == request.book_title)
    valid_request = db.execute(stmt).scalar_one_or_none()

    if valid_request:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Already requested book")

    # check if the user exists in database
    stmt = select(User).where(User.id == request.user_id)
    valid_user_id = db.execute(stmt).scalar_one_or_none()

    if not valid_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Invalid user ID"
        )

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
