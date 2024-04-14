from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db, get_current_admin_user

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)


@router.post(
    "/books",
    summary="도서 정보 등록",
)
async def create_book(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.put(
    "/books/{book_id}",
    summary="도서 정보 수정",
)
async def update_book(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.delete(
    "/books/{book_id}",
    summary="도서 정보 삭제",
)
async def delete_book(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.post(
    "/notifications",
    summary="알림 생성",
)
async def create_notification(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.get(
    "/book-requests",
    summary="도서 구매 요청 목록 조회",
)
async def list_book_requests(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.get(
    "/book-requests/{request_id}",
    summary="도서 구매 요청 상세 정보 조회",
)
async def get_book_request(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.put(
    "/book-requests/{request_id}",
    summary="도서 구매 요청 수정",
)
async def update_book_request(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.delete(
    "/book-requests/{request_id}",
    summary="도서 구매 요청 삭제",
)
async def delete_book_request(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.get(
    "/users",
    summary="전체 사용자 목록 조회",
)
async def list_users(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.put(
    "/users/{user_id}",
    summary="사용자 정보 수정",
)
async def update_user(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.delete(
    "/users/{user_id}",
    summary="사용자 정보 삭제",
)
async def delete_user(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.get(
    "/loans",
    summary="전체 대출 목록 조회",
)
async def list_loans(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.get(
    "/reservations",
    summary="전체 예약 목록 조회",
)
async def list_reservations(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.post(
    "/notices",
    summary="공지사항 등록",
)
async def create_notice(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.put(
    "/notices/{notice_id}",
    summary="공지사항 수정",
)
async def update_notice(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.delete(
    "/notices/{notice_id}",
    summary="공지사항 삭제",
)
async def delete_notice(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.get(
    "/settings",
    summary="시스템 설정 조회",
)
async def get_settings(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.put(
    "/settings",
    summary="시스템 설정 수정",
)
async def update_settings(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass
