from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import domain.schemas.admin_schemas as s
from dependencies import get_current_active_user, get_db
from domain.services.admin_service import *
from repositories.requested_book import RequestedBook

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)]
)


@router.put(
    "/{user_id}/book-requests/{requests_id}",
    summary="도서 구매 요청 수정",
    response_model=s.BookRequest,
    status_code=status.HTTP_200_OK
)
async def update_book_request(request_id: int, request_data: BookRequestUpdate, db: Session = Depends(get_db), get_current_active_user=Depends(get_current_active_user)):
    return update_item(RequestedBook, request_id, request_data, db)
