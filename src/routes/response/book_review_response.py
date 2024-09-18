from typing import List
from pydantic import BaseModel, Field

from domain.schemas.book_review_schemas import BookReviewByInfoId


class BookReviewListByInfoIdResponse(BaseModel):
    data: List[BookReviewByInfoId]
    count: int = Field(description="data 배열의 요소 개수")
