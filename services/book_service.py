from uuid import uuid4
from repository import book_repo

async def get_books(status=None, author=None, sort_by=None):
    books = book_repo.get_all_books()

    if status:
        books = [b for b in books if b["status"] == status]

    if author:
        books = [b for b in books if b["author"] == author]

    if sort_by:
        books = sorted(books, key=lambda x: x.get(sort_by))

    return books


async def get_book(book_id):
    return book_repo.get_book_by_id(book_id)


async def create_book(book_data):
    book = book_data.model_dump()
    book["id"] = uuid4()
    return book_repo.add_book(book)


async def remove_book(book_id):
    return book_repo.delete_book(book_id)