from repository import book_repo


async def get_books(status=None, author=None, sort_by=None, limit=10, offset=0):
    return book_repo.get_books(status, author, sort_by, limit, offset)


async def get_book(book_id):
    return book_repo.get_book_by_id(book_id)


async def create_book(book_data):
    data = book_data.model_dump()
    return book_repo.create_book(data)


async def remove_book(book_id):
    return book_repo.delete_book(book_id)