from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    isbn: str
    publication_date: str
    publisher: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    category_id: int


class BookSearchResult(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
