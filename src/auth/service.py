from datetime import timedelta


from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from config import Settings
from models import User
from auth.firebase import sign_in_with_email_and_password
from auth.token_service import create_jwt


async def login(request, db: Session):
    # Authenticate user
    # Check if user exists in Firebase
    firebase_response = await sign_in_with_email_and_password(request.email, request.password)
    try:
        localId = firebase_response["localId"]
        return localId
    except KeyError:
        error_message = firebase_response["error"]["message"]
        if error_message == "INVALID_EMAIL":
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        elif error_message == "INVALID_PASSWORD":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
        elif error_message == "USER_DISABLED":
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


# TODO: create jwt token을 token_service.py에 옮기고, 간략화할 것
# TODO: 회원가입 API 작성하기

    # Create JWT token
    # Create Access Token
    access_token_expires = timedelta(minutes=Settings().JWT_ACCESS_EXPIRATION_TIME_MINUTES)
    access_token = create_jwt(
        data={"sub": user.id},
        secret_key=Settings().JWT_SECRET_KEY,
        algorithm=Settings().JWT_ALGORITHM,
        expires_delta=access_token_expires
    )

    # Create Refresh Token
    refresh_token_expires = timedelta(minutes=Settings().JWT_REFRESH_EXPIRATION_TIME_MINUTES)
    refresh_token = create_jwt(
        data={"sub": user.id},
        secret_key=Settings().JWT_SECRET_KEY,
        algorithm=Settings().JWT_ALGORITHM,
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
