from fastapi import APIRouter, HTTPException, status
from typing import Optional
from uuid import UUID

from schemas.books import BookCreate
from services import book_service

router = APIRouter(prefix="/books", tags=["Books"])

# 1. GET all
@router.get("/")
async def get_books(
    status: Optional[str] = None,
    author: Optional[str] = None,
    sort_by: Optional[str] = None
):
    return await book_service.get_books(status, author, sort_by)


# 2. GET by ID
@router.get("/{book_id}")
async def get_book(book_id: UUID):
    book = await book_service.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


# 3. POST
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate):
    return await book_service.create_book(book)


# 4. DELETE (ідемпотентний)
@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: UUID):
    await book_service.remove_book(book_id)
    return