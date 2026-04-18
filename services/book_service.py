from repository import book_repo


def get_books(limit=10, offset=0):
    return book_repo.get_books(limit=limit, offset=offset)


def get_book(book_id):
    return book_repo.get_book_by_id(book_id)


def create_book(data):
    return book_repo.create_book(data)


def remove_book(book_id):
    return book_repo.delete_book(book_id)