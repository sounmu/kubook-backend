from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, ConfigDict

from dependencies import get_db


class ServiceSetting(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    service_begin: str
    service_end: str


router = APIRouter(
    prefix="/test",
    tags=["test"]
)


@router.get("/service-setting")
async def get_service_setting(db: Session = Depends(get_db)):
    return db.query(ServiceSetting).all()
