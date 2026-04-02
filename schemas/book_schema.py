from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
from enum import Enum

class BookStatus(str, Enum):
    available = "available"
    issued = "issued"

class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str
    description: Optional[str] = None
    status: BookStatus
    year: int

class Book(BookCreate):
    id: UUID