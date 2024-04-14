from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db

router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.get(
    "/search",
    summary="도서 검색",
)
async def search_books(db: Session = Depends(get_db)):
    pass


@router.get(
    "/categories/{category_id}",
    summary="카테고리별 도서 조회",
)
async def list_books_by_category(db: Session = Depends(get_db)):
    pass
