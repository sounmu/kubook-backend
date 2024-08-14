from typing import List

import admin.schemas as s
import models as m
from admin.service import *
from dependencies import get_current_admin, get_db
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/admin/books",
    tags=["admin/books"],
    dependencies=[Depends(get_current_admin),]
)
# =================== 도서 정보 =========================

@router.get(
    "/book-info",
    summary="도서 정보 목록 조회",
    response_model=List[s.BookInfoRes],
    status_code=status.HTTP_200_OK
)
async def get_list_book_info(db: Session = Depends(get_db)):
    return get_list(m.BookInfo, db)

@router.get(
    "/book-info/{book_info_id}",
    summary="도서 정보 조회",
    response_model=s.BookInfo,
    status_code=status.HTTP_200_OK
)
async def get_book_info(book_info_id: int, db: Session = Depends(get_db)):
    return get_item(m.BookInfo, book_info_id, db)

@router.post(
    "/book-info",
    summary="도서 정보 등록",
    response_model=s.BookInfo,
    status_code=status.HTTP_201_CREATED
)
async def create_book_info(book_info_data: s.BookInfoCreate, db: Session = Depends(get_db)):
    return create_item(m.BookInfo, book_info_data, db)

@router.patch(
    "/book-info/{book_info_id}",
    summary="도서 정보 수정",
    response_model=s.BookInfo,
    status_code=status.HTTP_200_OK
)
async def update_book_info(book_info_id: int, book_info_data: s.BookInfoUpdate, db: Session = Depends(get_db)):
    return update_item(m.BookInfo, book_info_id, book_info_data, db)

@router.delete(
    "/book-info/{book_info_id}",
    summary="도서 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book_info(book_info_id: int, db: Session = Depends(get_db)):
    return delete_item(m.BookInfo, book_info_id, db)

# =================== 책 정보 =========================

@router.get(
    "/books",
    summary="책 정보 목록 조회",
    response_model=List[s.BookRes],
    status_code=status.HTTP_200_OK
)
async def get_list_books(db: Session = Depends(get_db)):
    return get_list(m.Book, db)


@router.get(
    "/books/{book_id}",
    summary="책 정보 조회",
    response_model=s.Book,
    status_code=status.HTTP_200_OK
)
async def get_book_info(book_id: int, db: Session = Depends(get_db)):
    return get_item(m.Book, book_id, db)

@router.post(
    "/books",
    summary="책 정보 등록",
    response_model=s.Book,
    status_code=status.HTTP_201_CREATED
)
async def create_book(book_data: BookCreate, db: Session = Depends(get_db)):
    return create_item(m.Book, book_data, db)

@router.patch(
    "/books/{book_id}",
    summary="책 정보 수정",
    response_model=s.Book,
    status_code=status.HTTP_200_OK
)
async def update_book(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db)):
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
async def get_list_category(db: Session = Depends(get_db)):
    return get_list(m.BookCategory, db)

@router.get(
    "/category/{category_id}",
    summary="카테고리 정보 조회",
    response_model=s.Category,
    status_code=status.HTTP_200_OK
)
async def get_category(category_id: int, db: Session = Depends(get_db)):
    return get_item(m.BookCategory, category_id, db)

@router.post(
    "/category",
    summary="카테고리 생성",
    response_model=s.Category,
    status_code=status.HTTP_201_CREATED
)
async def create_category(category_data: CategoryCreate, db: Session = Depends(get_db)):
    return create_item(m.BookCategory, category_data, db)

@router.patch(
    "/category/{category_id}",
    summary="카테고리 정보 수정",
    response_model=s.Category,
    status_code=status.HTTP_200_OK
)
async def update_category(category_id: int, category_data: CategoryUpdate, db: Session = Depends(get_db)):
    return update_item(m.BookCategory, category_id, category_data, db)

@router.delete(
    "/category/{category_id}",
    summary="카테고리 정보 삭제",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_category(category_id: int, db: Session = Depends(get_db)):
    return delete_item(m.BookCategory, category_id, db)