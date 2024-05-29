from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from dependencies import get_db, get_current_admin 
from admin.service import *
import admin.schemas as s
import models as m

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

# =================== 관리자 =========================
@router.get(
    "/info/admin",
    summary="관리자 정보 목록 조회",
    response_model=List[s.AdminRes],
    status_code=status.HTTP_200_OK
)
async def get_list_admin(current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_list(m.Admin, db)

@router.get(
    "/info/admin/{admin_id}",
    summary="관리자 정보 조회",
    response_model=s.Admin,
    status_code=status.HTTP_200_OK
)
async def get_admin(admin_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_item(m.Admin, admin_id, db)

@router.post(
    "/info/admin",
    summary="관리자 정보 등록",
    response_model=s.Admin,
    status_code=status.HTTP_201_CREATED
)
async def create_admin(admin_data: s.AdminCreate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return create_item(m.Admin, admin_data, db) 

@router.patch(
    "/info/admin/{admin_id}",
    summary="관리자 정보 수정",
    response_model=s.Admin,
    status_code=status.HTTP_200_OK
)
async def update_admin(admin_id: int, admin_data: s.AdminUpdate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return update_item(m.Admin, admin_id, admin_data, db)

@router.delete(
    "/info/admin/{admin_id}",
    summary="관리자 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_admin(admin_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return delete_item(m.Admin, admin_id, db)

# =================== 도서 정보 =========================

@router.get(
    "/book-info",
    summary="도서 정보 목록 조회",
    response_model=List[s.BookInfoRes],
    status_code=status.HTTP_200_OK
)
async def get_list_book_info(current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_list(m.BookInfo, db)

@router.get(
    "/book-info/{book_info_id}",
    summary="도서 정보 조회",
    response_model=s.BookInfo,
    status_code=status.HTTP_200_OK
)
async def get_book_info(book_info_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_item(m.BookInfo, book_info_id, db)

@router.post(
    "/book-info",
    summary="도서 정보 등록",
    response_model=s.BookInfo,
    status_code=status.HTTP_201_CREATED
)
async def create_book_info(book_info_data: s.BookInfoCreate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return create_item(m.BookInfo, book_info_data, db)

@router.patch(
    "/book-info/{book_info_id}",
    summary="도서 정보 수정",
    response_model=s.BookInfo,
    status_code=status.HTTP_200_OK
)
async def update_book_info(book_info_id: int, book_info_data: s.BookInfoUpdate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return update_item(m.BookInfo, book_info_id, book_info_data, db)

@router.delete(
    "/book-info/{book_info_id}",
    summary="도서 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book_info(book_info_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return delete_item(m.BookInfo, book_info_id, db)

# =================== 책 정보 =========================

@router.get(
    "/books",
    summary="책 정보 목록 조회",
    response_model=List[s.BookRes],
    status_code=status.HTTP_200_OK
)
async def get_list_books(current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_list(m.Book, db)


@router.get(
    "/books/{book_id}",
    summary="책 정보 조회",
    response_model=s.Book,
    status_code=status.HTTP_200_OK
)
async def get_book_info(book_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_item(m.Book, book_id, db)

@router.post(
    "/books",
    summary="책 정보 등록",
    response_model=s.Book,
    status_code=status.HTTP_201_CREATED
)
async def create_book(book_data: BookCreate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return create_item(m.Book, book_data, db)

@router.patch(
    "/books/{book_id}",
    summary="책 정보 수정",
    response_model=s.Book,
    status_code=status.HTTP_200_OK
)
async def update_book(book_id: int, book_data: BookUpdate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return update_item(m.Book, book_id, book_data, db)

@router.delete(
    "/books/{book_id}",
    summary="책 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book(book_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return delete_item(m.Book, book_id, db)
# =================== 카테고리 =========================

@router.get(
    "/category",
    summary="전체 카테고리 목록 조회",
    response_model=List[s.CategoryRes],
    status_code=status.HTTP_200_OK
)
async def get_list_category(current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_list(m.BookCategory, db)

@router.get(
    "/category/{category_id}",
    summary="카테고리 정보 조회",
    response_model=s.Category,
    status_code=status.HTTP_200_OK
)
async def get_category(category_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_item(m.BookCategory, category_id, db)

@router.post(
    "/category",
    summary="카테고리 생성",
    response_model=s.Category,
    status_code=status.HTTP_201_CREATED
)
async def create_category(category_data: CategoryCreate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return create_item(m.BookCategory, category_data, db)

@router.patch(
    "/category/{category_id}",
    summary="카테고리 정보 수정",
    response_model=s.Category,
    status_code=status.HTTP_200_OK
)
async def update_category(category_id: int, category_data: CategoryUpdate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return update_item(m.BookCategory, category_id, category_data, db)

@router.delete(
    "/category/{category_id}",
    summary="카테고리 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_category(category_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return delete_item(m.BookCategory, category_id, db)

# =================== 도서 구매 요청 =========================

@router.get(
    "/book-requests",
    summary="도서 구매 요청 목록 조회",
    response_model=List[s.BookRequestRes],
    status_code=status.HTTP_200_OK
)
async def get_list_book_requests(current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_list(m.RequestedBook, db)

@router.get(
    "/book-requests/{request_id}",
    summary="도서 구매 요청 정보 조회",
    response_model=s.BookRequest,
    status_code=status.HTTP_200_OK
)
async def get_book_request(request_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_item(m.RequestedBook, request_id, db)

@router.patch(
    "/book-requests/{request_id}",
    summary="도서 구매 요청 수정",
    response_model=s.BookRequest,
    status_code=status.HTTP_200_OK
)
async def update_book_request(request_id: int, request_data: BookRequestUpdate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return update_item(m.RequestedBook, request_id, request_data, db)

@router.delete(
    "/book-requests/{request_id}",
    summary="도서 구매 요청 삭제(미개발)",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book_request(request_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return delete_item(m.RequestedBook, request_id, db)

# =================== 사용자 정보 =========================
@router.get(
    "/users",
    summary="전체 사용자 목록 조회",
    response_model=List[s.UserRes],
    status_code=status.HTTP_200_OK
)
async def get_list_user(current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_list(m.User, db)

@router.get(
    "/users/{user_id}",
    summary="사용자 정보 조회",
    response_model=s.User,
    status_code=status.HTTP_200_OK
)
async def get_user(user_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_item(m.User, user_id, db)

@router.patch(
    "/users/{user_id}",
    summary="사용자 정보 수정",
    response_model=s.User,
    status_code=status.HTTP_200_OK
)
async def update_user(user_id: int, user: s.UserUpdate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return update_item(m.User, user_id, user, db)

@router.delete(
    "/users/{user_id}",
    summary="사용자 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(user_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return delete_item(m.User, user_id, db)

# =================== 대출 정보 =========================
@router.get(
    "/loans",
    summary="전체 대출 목록 조회",
    response_model=List[s.LoanRes],
    status_code=status.HTTP_200_OK
)
async def get_list_loans(current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_list(m.Loan, db)

@router.get(
    "/loans/{loan_id}",
    summary="대출 정보 조회",
    response_model=s.Loan,
    status_code=status.HTTP_200_OK
)
async def get_loan(loan_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_item(m.Loan, loan_id, db)

@router.patch(
    "/loans/{loan_id}",
    summary="대출 정보 수정",
    response_model=s.Loan,
    status_code=status.HTTP_200_OK
)
async def update_loan(loan_id: int, loan: LoanUpdate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return update_item(m.Loan, loan_id, loan, db)

@router.delete(
    "/loans/{loan_id}",
    summary="대출 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_loan(loan_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return delete_item(m.Loan, loan_id, db)

# =================== 예약 정보 =========================
@router.get(
    "/reservations",
    summary="전체 예약 목록 조회",
    response_model=List[s.ReservationRes],
    status_code=status.HTTP_200_OK
)
async def get_list_reservations(current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_list(m.Reservation, db)

@router.get(
    "/reservations/{reservation_id}",
    summary="예약 정보 조회",
    response_model=s.Reservation,
    status_code=status.HTTP_200_OK
)
async def get_reservation(reservation_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_item(m.Reservation, reservation_id, db)

@router.patch(
    "/reservations/{reservation_id}",
    summary="예약 정보 수정",
    response_model=s.Reservation,
    status_code=status.HTTP_200_OK
)
async def update_reservation(reservation_id: int, reservation_data: ReservationUpdate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return update_item(m.Reservation, reservation_id, reservation_data, db)

@router.delete(
    "/reservations/{reservation_id}",
    summary="예약 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_reservation(reservation_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return delete_item(m.Reservation, reservation_id, db)

# =================== 공지사항 =========================
@router.get(
    "/notices",
    summary="전체 공지사항 목록 조회",
    response_model=List[s.NoticeRes],
    status_code=status.HTTP_200_OK
)
async def get_list_notices(current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_list(m.Notice, db)

@router.get(
    "/notices/{notice_id}",
    summary="공지사항 조회",
    response_model=s.Notice,
    status_code=status.HTTP_200_OK
)
async def get_notice(notice_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_item(m.Notice, notice_id, db)

@router.post(
    "/notices",
    summary="공지사항 등록",
    response_model=s.Notice,
    status_code=status.HTTP_201_CREATED
)
async def create_notice(notice_data: NoticeCreate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    notice_data.admin_id = current_user.admin.id
    return create_item(m.Notice, notice_data, db)

@router.patch(
    "/notices/{notice_id}",
    summary="공지사항 수정",
    response_model=s.Notice,
    status_code=status.HTTP_200_OK
)
async def update_notice(notice_id: int, notice_data: NoticeUpdate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    notice_data.admin_id = current_user.admin.id
    return update_item(m.Notice, notice_id, notice_data, db)

@router.delete(
    "/notices/{notice_id}",
    summary="공지사항 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_notice(notice_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return delete_item(m.Notice, notice_id, db)

# =================== 시스템 설정 =========================
@router.get(
    "/settings",
    summary="전체 시스템 설정 목록 조회",
    response_model=List[s.ServiceSetting],
    status_code=status.HTTP_200_OK
)
async def list_get_settings(current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_list(m.LibrarySetting, db)


@router.get(
    "/settings/{setting_id}",
    summary="시스템 설정 조회",
    response_model=s.ServiceSetting,
    status_code=status.HTTP_200_OK
)
async def get_settings(setting_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return get_item(m.LibrarySetting, setting_id, db)

@router.post(
    "/settings",
    summary="시스템 설정 등록",
    response_model=s.ServiceSetting,
    status_code=status.HTTP_201_CREATED
)
async def create_settings(settings: ServiceSettingCreate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return create_item(m.LibrarySetting, settings, db)


@router.patch(
    "/settings/{setting_id}",
    summary="시스템 설정 수정",
    response_model=s.ServiceSetting,
    status_code=status.HTTP_200_OK
)
async def update_settings(setting_id: int, setting: ServiceSettingUpdate, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return update_item(m.LibrarySetting, setting_id, setting, db)

@router.delete(
    "/settings/{setting_id}",
    summary="시스템 설정 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_settings(setting_id: int, current_user: m.User = Depends(get_current_admin), db: Session = Depends(get_db)):
    return delete_item(m.LibrarySetting, setting_id, db)

