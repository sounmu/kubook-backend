from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from config import Settings
from dependencies import get_db
import auth.schemas as auth_schemas
import auth.service as auth_service

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

settings = Settings()


@router.post(
    "/login",
    response_model=auth_schemas.LoginResponse,
    status_code=status.HTTP_200_OK,
    summary="로그인",
    description="""
    - 사용자가 이메일과 비밀번호를 입력한 후 로그인 버튼을 클릭
    - Firebase에 사용자 정보가 존재하지 않으면 (프론트에서) LMS에서 회원가입하라고 안내
    - Firebase에 사용자 정보가 존재할 경우 쿠책책의 DB에 사용자 정보가 있는지 확인
    - 만약 사용자 정보가 있다면 로그인 처리
    - 사용자 정보가 없다면 회원가입 페이지로 이동
        - 그런데 회원가입 페이지에서 추가로 입력할 내용이 거의 없어서 회원가입 API POST /auth/register는 Deprecated 처리함
        - 추후 회원가입 시 기입할 정보가 늘어난다면 POST /auth/register를 다시 활성화할 것
    """,
    response_description={
        status.HTTP_200_OK: {"description": "Login successful"},
        status.HTTP_404_NOT_FOUND: {"description": "User not found"},
        status.HTTP_401_UNAUTHORIZED: {"description": "Invalid password"},
        status.HTTP_403_FORBIDDEN: {"description": "User disabled"},
    }
)
async def login(
    request: auth_schemas.LoginRequest,
    db: Session = Depends(get_db)
):
    return await auth_service.login(request, db)


@router.post(
    "/register",
    summary="회원 가입",
    deprecated=True
)
async def signup(db: Session = Depends(get_db)):
    pass
