from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db_session
from models import User


def get_db():
    db = next(get_db_session())
    try:
        yield db
    finally:
        db.close()


async def get_current_user():
    pass


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    pass


async def get_current_admin_user(current_user: User = Depends(get_current_user)):
    pass
