from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from dependencies import get_db, get_current_admin_user
from .schemas import *

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

# =================== 도서 정보 =========================

@router.get(
    "/book-info",
    summary="도서 정보 목록 조회",
    response_model=List[BookInfo],
    status_code=status.HTTP_200_OK
)
async def get_list_book_info(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/book-info/{book_info_id}",
    summary="도서 정보 조회",
    response_model=BookInfo,
    status_code=status.HTTP_200_OK
)
async def get_book_info(book_info_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.post(
    "/book-info",
    summary="도서 정보 등록",
    response_model=BookInfo,
    status_code=status.HTTP_201_CREATED
)
async def create_book_info(book_info: BookInfoCreate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/book-info/{book_info_id}",
    summary="도서 정보 수정",
    response_model=BookInfo,
    status_code=status.HTTP_200_OK
)
async def update_book_info(book_info_id: int, book_info: BookInfoUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.delete(
    "/book-info/{book_info_id}",
    summary="도서 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book_info(book_info_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

# =================== 책 정보 =========================

@router.get(
    "/books",
    summary="책 정보 목록 조회",
    response_model=List[Book],
    status_code=status.HTTP_200_OK
)
async def get_list_books(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/books/{book_id}",
    summary="책 정보 조회",
    response_model=Book,
    status_code=status.HTTP_200_OK
)
async def get_book_info(book_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.post(
    "/books",
    summary="책 정보 등록",
    response_model=Book,
    status_code=status.HTTP_201_CREATED
)
async def create_book(book: BookCreate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/books/{book_id}",
    summary="책 정보 수정",
    response_model=Book,
    status_code=status.HTTP_200_OK
)
async def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.delete(
    "/books/{book_id}",
    summary="책 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book(book_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass
# =================== 카테고리 =========================

@router.get(
    "/category",
    summary="전체 카테고리 목록 조회",
    response_model=List[Category],
    status_code=status.HTTP_200_OK
)
async def get_list_category(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/category/{category_id}",
    summary="카테고리 정보 조회",
    response_model=Category,
    status_code=status.HTTP_200_OK
)
async def get_category(category_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.post(
    "/category",
    summary="카테고리 생성",
    response_model=Category,
    status_code=status.HTTP_201_CREATED
)
async def create_category(category: CategoryCreate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/category/{category_id}",
    summary="카테고리 정보 수정",
    response_model=Category,
    status_code=status.HTTP_200_OK
)
async def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.delete(
    "/category/{category_id}",
    summary="카테고리 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_category(category_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

# =================== 도서 구매 요청 =========================

@router.get(
    "/book-requests",
    summary="도서 구매 요청 목록 조회",
    response_model=List[BookRequest],
    status_code=status.HTTP_200_OK
)
async def get_list_book_requests(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/book-requests/{request_id}",
    summary="도서 구매 요청 정보 조회",
    response_model=BookRequest,
    status_code=status.HTTP_200_OK
)
async def get_book_request(request_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/book-requests/{request_id}",
    summary="도서 구매 요청 수정",
    response_model=BookRequest,
    status_code=status.HTTP_200_OK
)
async def update_book_request(request_id: int, request: BookRequestUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.delete(
    "/book-requests/{request_id}",
    summary="도서 구매 요청 삭제(미개발)",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book_request(request_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

# =================== 사용자 정보 =========================
@router.get(
    "/users",
    summary="전체 사용자 목록 조회",
    response_model=List[User],
    status_code=status.HTTP_200_OK
)
async def get_list_user(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/users/{user_id}",
    summary="사용자 정보 조회",
    response_model=User,
    status_code=status.HTTP_200_OK
)
async def get_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/users/{user_id}",
    summary="사용자 정보 수정",
    response_model=User,
    status_code=status.HTTP_200_OK
)
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.delete(
    "/users/{user_id}",
    summary="사용자 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

# =================== 대출 정보 =========================
@router.get(
    "/loans",
    summary="전체 대출 목록 조회",
    response_model=List[Loan],
    status_code=status.HTTP_200_OK
)
async def get_list_loans(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/loans/{loan_id}",
    summary="대출 정보 조회",
    response_model=Loan,
    status_code=status.HTTP_200_OK
)
async def get_loan(loan_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/loans/{loan_id}",
    summary="대출 정보 수정",
    response_model=Loan,
    status_code=status.HTTP_200_OK
)
async def update_loan(loan_id: int, loan: LoanUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.delete(
    "/loans/{loan_id}",
    summary="대출 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_loan(loan_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

# =================== 예약 정보 =========================
@router.get(
    "/reservations",
    summary="전체 예약 목록 조회",
    response_model=List[Reservation],
    status_code=status.HTTP_200_OK
)
async def get_list_reservations(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/reservations/{reservation_id}",
    summary="예약 정보 조회",
    response_model=Reservation,
    status_code=status.HTTP_200_OK
)
async def get_reservation(reservation_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/reservations/{reservation_id}",
    summary="예약 정보 수정",
    response_model=Reservation,
    status_code=status.HTTP_200_OK
)
async def update_reservation(reservation_id: int, reservation: ReservationUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.delete(
    "/reservations/{reservation_id}",
    summary="예약 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_reservation(reservation_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

# =================== 공지사항 =========================
@router.get(
    "/notices",
    summary="전체 공지사항 목록 조회",
    response_model=List[Notice],
    status_code=status.HTTP_200_OK
)
async def get_list_notices(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/notices/{notice_id}",
    summary="공지사항 조회",
    response_model=Notice,
    status_code=status.HTTP_200_OK
)
async def get_notice(notice_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.post(
    "/notices",
    summary="공지사항 등록",
    response_model=Notice,
    status_code=status.HTTP_201_CREATED
)
async def create_notice(notice: NoticeCreate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/notices/{notice_id}",
    summary="공지사항 수정",
    response_model=Notice,
    status_code=status.HTTP_200_OK
)
async def update_notice(notice_id: int, notice: NoticeUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.delete(
    "/notices/{notice_id}",
    summary="공지사항 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_notice(notice_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

# =================== 시스템 설정 =========================
@router.get(
    "/settings",
    summary="전체 시스템 설정 목록 조회",
    response_model=List[ServiceSetting],
    status_code=status.HTTP_200_OK
)
async def list_get_settings(db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.get(
    "/settings/{setting_id}",
    summary="시스템 설정 조회",
    response_model=ServiceSetting,
    status_code=status.HTTP_200_OK
)
async def get_settings(setting_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.post(
    "/settings",
    summary="시스템 설정 등록",
    response_model=ServiceSetting,
    status_code=status.HTTP_201_CREATED
)
async def create_settings(settings: ServiceSettingCreate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.patch(
    "/settings/{setting_id}",
    summary="시스템 설정 수정",
    response_model=ServiceSetting,
    status_code=status.HTTP_200_OK
)
async def update_settings(setting_id: int, settings: ServiceSettingUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass

@router.delete(
    "/settings/{setting_id}",
    summary="시스템 설정 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_settings(setting_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_admin_user)):
    pass
