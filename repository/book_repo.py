from models.book_model import books_db
def get_all_books():
    return books_db

def get_book_by_id(book_id):
    return next((b for b in books_db if str(b["id"]) == str(book_id)), None)

def add_book(book: dict):
    books_db.append(book)
    return book

def delete_book(book_id):
    global books_db
    initial_len = len(books_db)
    books_db = [b for b in books_db if str(b["id"]) != str(book_id)]
    return len(books_db) < initial_len