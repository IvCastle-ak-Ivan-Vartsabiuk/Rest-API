from bson import ObjectId


def serialize(book):
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "description": book.get("description"),
        "status": book["status"],
        "year": book["year"]
    }


def get_books(db, status=None, author=None, sort_by=None, limit=10, offset=0):
    query = {}

    if status:
        query["status"] = status

    if author:
        query["author"] = author

    cursor = db.books.find(query)

    if sort_by == "title":
        cursor = cursor.sort("title", 1)
    elif sort_by == "year":
        cursor = cursor.sort("year", 1)

    books = cursor.skip(offset).limit(limit)

    return [serialize(book) for book in books]


def get_book_by_id(db, book_id):
    book = db.books.find_one({"_id": ObjectId(book_id)})
    return serialize(book) if book else None


def create_book(db, data):
    result = db.books.insert_one(data)
    book = db.books.find_one({"_id": result.inserted_id})
    return serialize(book)


def delete_book(db, book_id):
    db.books.delete_one({"_id": ObjectId(book_id)})
    return True