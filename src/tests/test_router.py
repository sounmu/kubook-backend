from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, ConfigDict

from dependencies import get_db

from models import ServiceSetting

router = APIRouter(
    prefix="/test",
    tags=["test"]
)

class ServiceSetting(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    service_begin: str
    service_end: str

@router.get("/service-setting")
async def get_service_setting(db: Session = Depends(get_db)):
    return db.query(ServiceSetting).all()
