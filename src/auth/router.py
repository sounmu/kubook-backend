from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db
from auth import service as auth_service

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.get("/users")
async def list_users():
    users = await auth_service.get_all_users()
    return users


@router.post(
    "/login",
    summary="로그인",
)
async def login(db: Session = Depends(get_db)):
    pass


@router.post(
    "/",
    summary="회원 가입",
)
async def signup(db: Session = Depends(get_db)):
    pass
