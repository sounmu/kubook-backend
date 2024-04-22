from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime, Date, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    auth_id = Column(String(50), unique=True, nullable=False)
    user_name = Column(String(45), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_valid = Column(Boolean, nullable=False, default=True)

    requested_books = relationship("RequestedBook", back_populates="user")
    admin = relationship("Admin", back_populates="user")
    book_reviews = relationship("BookReview", back_populates="user")
    reservations = relationship("Reservation", back_populates="user")
    loans = relationship("Loan", back_populates="user")


class RequestedBook(Base):
    __tablename__ = "requested_book"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    book_title = Column(String(255), nullable=False)
    publication_year = Column(Integer)
    reject_reason = Column(Text, nullable=True)
    request_link = Column(String(100), nullable=False)
    reason = Column(Text, nullable=False)
    processing_status = Column(Integer, nullable=False, default=0)
    request_date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_valid = Column(Boolean, nullable=False, default=True)

    user = relationship("User", back_populates="requested_books")


class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    admin_status = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_valid = Column(Boolean, nullable=False, default=False)

    user = relationship("User", back_populates="admin")
    notices = relationship("Notice", back_populates="admin")


class Notice(Base):
    __tablename__ = "notice"

    id = Column(Integer, primary_key=True, index=True)
    admin_id = Column(Integer, ForeignKey("admin.id"), nullable=False)
    user_id = Column(Integer)
    title = Column(String(255), nullable=False)
    notice_content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_valid = Column(Boolean, nullable=False, default=True)

    admin = relationship("Admin", back_populates="notices")


class BookCategory(Base):
    __tablename__ = "book_category"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(5), nullable=False)
    name = Column(String(50), nullable=False)
    is_valid = Column(Boolean, nullable=False, default=True)

    books = relationship("BookInfo", back_populates="category")


class BookInfo(Base):
    __tablename__ = "book_info"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    subtitle = Column(String(255))
    author = Column(String(100), nullable=False)
    publisher = Column(String(45), nullable=False)
    publication_year = Column(Integer, nullable=False)
    image_url = Column(String(255))
    category_id = Column(Integer, ForeignKey("book_category.id"), nullable=False)
    copied = Column(String(100))
    version = Column(String(45))
    major = Column(Boolean, default=False)
    language = Column(String(10), nullable=False, default="한국어")
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_valid = Column(Boolean, nullable=False, default=True)

    category = relationship("BookCategory", back_populates="books")
    book_stat = relationship("BookStat", back_populates="book_info")
    book_reviews = relationship("BookReview", back_populates="book_info")
    books = relationship("Book", back_populates="book_info")


class BookStat(Base):
    __tablename__ = "book_stat"

    id = Column(Integer, primary_key=True, index=True)
    book_info_id = Column(Integer, ForeignKey("book_info.id"), nullable=False)
    review_count = Column(Integer, nullable=False, default=0)
    loan_count = Column(Integer, nullable=False, default=0)

    book_info = relationship("BookInfo", back_populates="book_stat")


class BookReview(Base):
    __tablename__ = "book_review"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    book_info_id = Column(Integer, ForeignKey("book_info.id"), nullable=False)
    review_content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_valid = Column(Boolean, nullable=False, default=True)

    user = relationship("User", back_populates="book_reviews")
    book_info = relationship("BookInfo", back_populates="book_reviews")


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    book_info_id = Column(Integer, ForeignKey("book_info.id"), nullable=False)
    book_status = Column(Boolean, nullable=False, default=True)
    note = Column(String(255), default=None)
    donor_name = Column(String(255), default=None)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_valid = Column(Boolean, nullable=False, default=False)

    book_info = relationship("BookInfo", back_populates="books")
    reservations = relationship("Reservation", back_populates="book")
    loans = relationship("Loan", back_populates="book")


class Reservation(Base):
    __tablename__ = "reservation"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    reservation_date = Column(DateTime, nullable=False, default=func.current_timestamp())
    reservation_status = Column(Integer, nullable=0)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_valid = Column(Boolean, nullable=False, default=True)

    book = relationship("Book", back_populates="reservations")
    user = relationship("User", back_populates="reservations")


class Loan(Base):
    __tablename__ = "loan"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    loan_date = Column(Date, nullable=False)
    extend_status = Column(Boolean, nullable=False, default=False)
    expected_return_date = Column(Date, nullable=False)
    return_status = Column(Boolean, nullable=False, default=False)
    return_date = Column(Date)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.current_timestamp(), onupdate=func.current_timestamp())
    is_valid = Column(Boolean, nullable=False, default=True)

    book = relationship("Book", back_populates="loans")
    user = relationship("User", back_populates="loans")


class ServiceSetting(Base):
    __tablename__ = "service_setting"

    id = Column(Integer, primary_key=True, index=True)
    service_begin = Column(DateTime, nullable=False)
    service_end = Column(DateTime, nullable=False)


class LoanSetting(Base):
    __tablename__ = "loan_setting"

    id = Column(Integer, primary_key=True, index=True)
    max_loan_count = Column(Integer, nullable=False)
    loan_period = Column(Integer, nullable=False)
    extend_period = Column(Integer, nullable=False)


class RequestSetting(Base):
    __tablename__ = "request_setting"

    id = Column(Integer, primary_key=True, index=True)
    max_request_count = Column(Integer, nullable=False)
    max_request_price = Column(Integer, nullable=False)


class ReservationSetting(Base):
    __tablename__ = "reservation_setting"

    id = Column(Integer, primary_key=True, index=True)
    max_books_per_user = Column(Integer, nullable=False)
    max_users_per_book = Column(Integer, nullable=False)
