from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from auth.firebase_login import sign_in_with_email_and_password
from models import User

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


class LoginRequest(BaseModel):
    email: str
    password: str


class UserInfo(BaseModel):
    id: int
    user_name: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserInfo


@router.post(
    "/login",
    response_model=LoginResponse,
    summary="로그인",
)
async def login(
    request: LoginRequest,
    # db: Session = Depends(get_db)
):
    firebase_response = await sign_in_with_email_and_password(request.email, request.password)

    if firebase_response == "INVALID_EMAIL":
        raise HTTPException(status_code=404, detail="User not found")
    elif firebase_response == "INVALID_PASSWORD":
        raise HTTPException(status_code=401, detail="Invalid password")
    elif firebase_response == "USER_DISABLED":
        raise HTTPException(status_code=403, detail="User disabled")

    local_id = firebase_response
    # user = db.query(User).filter(User.auth_id == local_id).first()
    temp_user = "민재"   # 임시 사용자 정보
    temp_user = None
    if not temp_user:
        raise HTTPException(status_code=302, detail="/auth/register")

    return {
        "access_token": "example_access_token",
        "token_type": "bearer",
        "user": {
            "id": "0",
            "email": "권민재"
        }
    }


@router.post(
    "/register",
    summary="회원 가입",
)
async def signup(db: Session = Depends(get_db)):
    return {"message": "회원 가입"}
