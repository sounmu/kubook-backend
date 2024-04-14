from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_db, get_current_active_user

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"]
)


@router.get(
    "/",
    summary="알림 목록 조회",
)
async def list_notifications(db: Session = Depends(get_db), current_user=Depends(get_current_active_user)):
    pass


@router.get(
    "/{notification_id}",
    summary="알림 상세 정보 조회",
)
async def get_notification(db: Session = Depends(get_db), current_user=Depends(get_current_active_user)):
    pass


@router.delete(
    "/{notification_id}",
    summary="알림 삭제",
)
async def delete_notification(db: Session = Depends(get_db), current_user=Depends(get_current_active_user)):
    pass
