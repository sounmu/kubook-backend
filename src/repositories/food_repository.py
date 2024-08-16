from sqlalchemy import (TIMESTAMP, Boolean, Column, ForeignKey, Integer,
                        String, Text)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .base import Base


class Food(Base):
    __tablename__ = "food"

    id = Column(Integer, primary_key=True, index=True)
    food_name = Column(String(255), nullable=False)
    food_type = Column(String(20), nullable=False)
    food_price = Column(Integer, nullable=False)
    food_description = Column(Text, nullable=False)
    food_image_url = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now())
