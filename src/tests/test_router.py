from typing import List
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, ConfigDict

from dependencies import get_db

from models import LibrarySetting

router = APIRouter(
    prefix="/test",
    tags=["test"]
)


class LibrarySettings(BaseModel):
    id: int
    name: str
    value: str
    data_type: str
    description: str
    created_at: datetime
    updated_at: datetime
    is_valid: bool


@router.get(
    "/library-setting",
    response_model=List[LibrarySettings],
    status_code=status.HTTP_200_OK,
    description="""
    이 API는 get_db로 DB 연결을 테스트하기 위한 API입니다.
    모든 도서관 설정을 조회합니다.
    """,
    summary="모든 도서관 설정 조회",
    response_description={
        200: {"description": "모든 도서관 설정 조회 성공"},
        500: {"description": "서버 에러"}
    }
)
async def get_library_setting(db: Session = Depends(get_db)):
    library_settings = db.query(LibrarySetting).all()
    return library_settings
