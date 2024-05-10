from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from database import get_db_session
from config import Settings
from models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
settings = Settings()


def get_db():
    try:
        session = get_db_session()
        yield session
    finally:
        session.close()


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user


def get_current_admin(user: User = Depends(get_current_user)):
    if not user.admin or not user.admin.admin_status:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges"
        )
    return user

"""
get_current_admin 사용법 예시

def example(current_user: User = Depends(get_current_admin)):
    return {"message": "Welcome Admin!"}
"""