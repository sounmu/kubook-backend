from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .base import Base


class Loan(Base):
    __tablename__ = "loan"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    loan_date = Column(DateTime, nullable=False)
    due_date = Column(DateTime, nullable=False)
    extend_status = Column(String(20), nullable=False, default="FALSE")
    return_status = Column(String(20), nullable=False, default="FALSE")
    return_date = Column(DateTime, nullable=True)
    overdue_days = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, nullable=False, default=False)

    book = relationship("Book", back_populates="loans")
    user = relationship("User", back_populates="loans")
