from .base import Base
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql import func


class BookStat(Base):
    __tablename__ = 'book_stat'

    book_info_id = Column(Integer, ForeignKey('book_info.id'), primary_key=True)
    review_count = Column(Integer)
    loan_count = Column(Integer)

    book_info = relationship("BookInfo", viewonly=True)
