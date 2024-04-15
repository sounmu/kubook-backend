from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from dependencies import get_db
from auth.firebase_login import sign_in_with_email_and_password
from models import User
from config import Settings

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

settings = Settings()


def create_jwt(
    data: dict,
    secret_key: str,
    algorithm: str,
    expires_delta: timedelta | None = None
):
    """
    Create a JWT token with the given data.

    Args:
        data (dict): The data to be encoded in the token.
        secret_key (str): The secret key used to sign the token.
        algorithm (str): The algorithm used to sign the token.
        expires_delta (timedelta | None, optional): The expiration time for the token. Defaults to None, which means the token will expire in 15 minutes.

    Returns:
        str: The encoded JWT token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


class LoginRequest(BaseModel):
    email: str
    password: str


class UserInfo(BaseModel):
    id: int
    user_name: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class LoginResponse(BaseModel):
    token: Token
    user: UserInfo


@router.post(
    "/login",
    response_model=LoginResponse,
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
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    # Authenticate user
    # Check if user exists in Firebase
    firebase_response = await sign_in_with_email_and_password(request.email, request.password)

    if firebase_response == "INVALID_EMAIL":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    elif firebase_response == "INVALID_PASSWORD":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    elif firebase_response == "USER_DISABLED":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User disabled")

    # Check if user information exists in the DB
    local_id = firebase_response
    user = db.query(User).filter(User.auth_id == local_id).first()

    # If user information does not exist in the DB, create a new user
    if user is None:
        user = User(
            auth_id=local_id,
            user_name="권민재",
            email=request.email
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    # Create JWT token
    # Create Access Token
    access_token_expires = timedelta(minutes=settings.JWT_ACCESS_EXPIRATION_TIME_MINUTES)
    access_token = create_jwt(
        data={"sub": user.id},
        secret_key=settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
        expires_delta=access_token_expires
    )

    # Create Refresh Token
    refresh_token_expires = timedelta(minutes=settings.JWT_REFRESH_EXPIRATION_TIME_MINUTES)
    refresh_token = create_jwt(
        data={"sub": user.id},
        secret_key=settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
        expires_delta=refresh_token_expires
    )

    return {
        "token": {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        },
        "user": {
            "id": user.id,
            "user_name": user.user_name
        }
    }


@router.post(
    "/register",
    summary="회원 가입",
    deprecated=True
)
async def signup(db: Session = Depends(get_db)):
    pass
