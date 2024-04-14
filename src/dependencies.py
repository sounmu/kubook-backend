from fastapi import Depends
from sqlalchemy.orm import Session

from .database import get_db_session


def get_db():
    db = next(get_db_session())
    try:
        yield db
    finally:
        db.close()
