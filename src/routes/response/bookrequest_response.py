from datetime import datetime

from pydantic import BaseModel, Field


class RouteResPostBookRequest(BaseModel):
    request_id: int = Field(title="purchase_id", description="구매 요청 정보 id", example=1, gt=0)
    user_id: int = Field(title="user_id", description="구매 요청한 사용자 id", example=1, gt=0)
    book_title: str = Field(title="book_title", description="구매 요청한 책 제목", example="book1")
    publication_year: int = Field(title="publication_year", description="출판 년도", example=2024, gt=0)
    request_link: str = Field(title="request_link", description="구매 요청 링크", example="https://www.example.com/request")
    requested_at: datetime = Field(title="requested_at", description="구매 요청한 날짜",
                                   example=datetime.today().date())
    reason: str = Field(title="reason", description="구매 요청 이유", example="학습 목적")
    processing_status: int = Field(title="processing_status", description="구매 요청 처리 상태", example=0, ge=0, le=3)
