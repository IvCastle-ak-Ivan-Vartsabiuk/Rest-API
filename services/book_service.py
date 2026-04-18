from repository import book_repo_mongo


async def get_books(db, status=None, author=None, sort_by=None, limit=10, offset=0):
    return book_repo_mongo.get_books(db, status, author, sort_by, limit, offset)


async def get_book(db, book_id):
    return book_repo_mongo.get_book_by_id(db, book_id)


async def create_book(db, book_data):
    data = book_data.model_dump()
    return book_repo_mongo.create_book(db, data)


async def remove_book(db, book_id):
    return book_repo_mongo.delete_book(db, book_id)