from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, ConfigDict

from dependencies import get_db

from models import ServiceSetting

router = APIRouter(
    prefix="/test",
    tags=["test"]
)


class ServiceSettings(BaseModel):
    id: int
    service_begin: datetime
    service_end: datetime


@router.get(
    "/service-setting",
    response_model=ServiceSettings,
)
async def get_service_setting(db: Session = Depends(get_db)):
    service_setting = db.query(ServiceSetting).first()
    return service_setting
