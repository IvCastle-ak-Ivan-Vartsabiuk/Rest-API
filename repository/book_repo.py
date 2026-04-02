from models.book_model import Book
from db.database import SessionLocal


def get_books(status=None, author=None, sort_by=None, limit=10, cursor=None):
    db = SessionLocal()

    query = db.query(Book)

    if status:
        query = query.filter(Book.status == status)

    if author:
        query = query.filter(Book.author == author)

    if cursor is not None:
        query = query.filter(Book.id > cursor)

    if sort_by == "title":
        query = query.order_by(Book.title)
    elif sort_by == "year":
        query = query.order_by(Book.year)
    else:
        query = query.order_by(Book.id)

    return query.limit(limit).all()


def get_book_by_id(book_id):
    db = SessionLocal()
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(data: dict):
    db = SessionLocal()
    book = Book(**data)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def delete_book(book_id):
    db = SessionLocal()
    book = db.query(Book).filter(Book.id == book_id).first()

    if book:
        db.delete(book)
        db.commit()

    return True  # ідемпотентність