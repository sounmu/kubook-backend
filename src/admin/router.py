from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db, get_current_admin_user

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

# =================== 도서 정보 =========================

@router.get(
    "/book-info",
    summary="도서 정보 목록 조회",
)
async def get_list_book_info(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.get(
    "/book-info/{book_info_id}",
    summary="도서 정보 조회",
)
async def get_book_info(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.post(
    "/book_info",
    summary="도서 정보 등록",
)
async def create_book_info(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/book_info/{book_info_id}",
    summary="도서 정보 수정",
)
async def update_book_info(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.delete(
    "/book_info/{book_info_id}",
    summary="도서 정보 삭제",
)
async def delete_book_info(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

# =================== 책 정보 =========================

@router.get(
    "/book-info",
    summary="책 정보 목록 조회",
)
async def get_list_book_info(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.get(
    "/book-info/{book_info_id}",
    summary="책 정보 조회",
)
async def get_book_info(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.post(
    "/books",
    summary="책 정보 등록",
)
async def create_book(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.patch(
    "/book/{book_id}",
    summary="책 정보 수정",
)
async def update_book(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.delete(
    "/books/{book_id}",
    summary="책 정보 삭제",
)
async def delete_book(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

# =================== 카테고리 =========================

@router.get(
    "/category",
    summary="전체 카테고리 목록 조회",
)
async def get_list_category(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/category/{category_id}",
    summary="카테고리 정보 조회",
)
async def get_category(category_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.post(
    "/category",
    summary="카테고리 생성",
)
async def create_category(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/category/{category_id}",
    summary="카테고리 정보 수정",
)
async def update_category(category_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.delete(
    "/category/{category_id}",
    summary="카테고리 정보 삭제",
)
async def delete_category(category_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

# =================== 도서 구매 요청 =========================

@router.get(
    "/book-requests",
    summary="도서 구매 요청 목록 조회",
)
async def get_list_book_requests(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.get(
    "/book-requests/{request_id}",
    summary="도서 구매 요청 상세 정보 조회",
)
async def get_book_request(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.patch(
    "/book-requests/{request_id}",
    summary="도서 구매 요청 수정",
)
async def update_book_request(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.delete(
    "/book-requests/{request_id}",
    summary="도서 구매 요청 삭제(미개발)",
)
async def delete_book_request(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


# =================== 사용자 정보 =========================

@router.get(
    "/users",
    summary="전체 사용자 목록 조회",
)
async def get_list_user(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/users/{user_id}",
    summary="사용자 정보 조회",
)
async def get_user(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.patch(
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


# =================== 대출 정보 =========================

@router.get(
    "/loans",
    summary="전체 대출 목록 조회",
)
async def get_list_loans(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.get(
    "/loans/{loan_id}",
    summary="대출 정보 조회",
)
async def get_loan(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/loans/{loan_id}",
    summary="대출 정보 수정",
)
async def update_loan(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.delete(
    "/loans/{loan_id}",
    summary="대출 정보 삭제",
)
async def delete_loan(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

# =================== 예약 정보 =========================

@router.get(
    "/reservations",
    summary="전체 예약 목록 조회",
)
async def get_list_reservations(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/reservations/{reservation_id}",
    summary="예약 정보 조회",
)
async def get_reservation(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/reservations/{reservation_id}",
    summary="예약 정보 수정",
)
async def update_reservation(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.delete(
    "/reservations/{reservation_id}",
    summary="예약 정보 삭제",
)
async def delete_reservatione(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

# =================== 공지사항 =========================
@router.get(
    "/notices",
    summary="전체 공지사항 목록 조회",
)
async def get_list_notices(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/notices/{notice_id}",
    summary="공지사항 조회",
)
async def get_notice(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.post(
    "/notices",
    summary="공지사항 등록",
)
async def create_notice(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass


@router.patch(
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

# =================== 시스템 설정 =========================
@router.get(
    "/settings",
    summary="시스템 설정 조회",
)
async def get_settings(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.post(
    "/settings",
    summary="시스템 설정 등록",
)
async def create_settings(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/settings",
    summary="시스템 설정 수정",
)
async def update_settings(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.delete(
    "/settings",
    summary="시스템 설정 삭제",
)
async def delete_settings(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass