from datetime import datetime as _datetime

from typing import List
from pydantic import BaseModel, Field

from domain.schemas.book_review_schemas import BookReviewItem


class BookReviewListResponse(BaseModel):
    """
    ReviewListResponse 모델은 리뷰 항목들의 목록과 해당 목록에 포함된 항목 개수를 반환하는 응답 구조입니다.

    Attributes:
        data (List[BookReviewItem]): 리뷰 항목의 목록을 담고 있는 배열입니다.
        count (int): data 배열의 요소 개수를 나타냅니다.
    """
    data: List[BookReviewItem]
    count: int = Field(description="data 배열의 요소 개수")


class BookReviewCreateResponse(BaseModel):
    review_id: int = Field(title="book_review_id", description="리뷰 id", example=1, gt=0)
    user_id: int = Field(title="user_id", description="리뷰한 사용자 ID", example=1, gt=0)
    user_name: str = Field(title="user_name", description="리뷰한 사용자 이름")
    book_info_id: int = Field(title="book_info_id", description="리뷰한 책 정보 ID", example=1, gt=0)
    review_content: str = Field(title="review_content", description="리뷰 내용")
    created_at: _datetime = Field(title="create_at", description="생성일시", example=_datetime.now())
