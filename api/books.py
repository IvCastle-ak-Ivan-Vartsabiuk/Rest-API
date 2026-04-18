from fastapi import APIRouter, HTTPException, status, Query, Depends
from typing import Optional
from uuid import UUID

from schemas.book_schema import BookCreate
from services import book_service
from db.mongo import get_db

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/")
async def get_books(
    status: Optional[str] = None,
    author: Optional[str] = None,
    sort_by: Optional[str] = None,
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
    db=Depends(get_db)
):
    return await book_service.get_books(db, status, author, sort_by, limit, offset)


@router.get("/{book_id}")
async def get_book(book_id: str, db=Depends(get_db)):
    book = await book_service.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate, db=Depends(get_db)):
    return await book_service.create_book(db, book)


@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: str, db=Depends(get_db)):
    await book_service.remove_book(db, book_id)
    return