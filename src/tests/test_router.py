from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from dependencies import get_db

from models import ServiceSetting
# class ServiceSetting(BaseModel):
#     service_begin: str
#     service_end: str

#     class Config:
#         orm_mode = True


router = APIRouter(
    prefix="/test",
    tags=["test"]
)


@router.get("/service-setting")
async def get_service_setting(db: Session = Depends(get_db)):
    return db.query(ServiceSetting).all()
