from .base import Base
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql import func


class LibrarySetting(Base):
    __tablename__ = "library_setting"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    value = Column(String(50), nullable=False)
    data_type = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_valid = Column(Boolean, nullable=False, default=True)
