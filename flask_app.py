from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger

from db.base import Base
from db.database import engine
from models.book_model import Book


Base.metadata.create_all(bind=engine)

from services.book_service import get_books, get_book, create_book, remove_book

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

import uuid


def to_dict(obj):
    if obj is None:
        return None
    d = obj.__dict__.copy()
    d.pop('_sa_instance_state', None)

    # Перетворюємо всі UUID поля на рядки
    for key, value in d.items():
        if isinstance(value, uuid.UUID):
            d[key] = str(value)

    return d

class BookListResource(Resource):
    def get(self):
        """
        Get books
        ---
        parameters:
          - name: limit
            in: query
            type: integer
          - name: offset
            in: query
            type: integer
        responses:
          200:
            description: List of books
        """
        limit = request.args.get("limit", 10, type=int)
        offset = request.args.get("offset", 0, type=int)

        books = get_books(limit=limit, offset=offset)
        # Перетворюємо кожну книгу в чистий словник
        return [to_dict(book) for book in books]

    def post(self):
        """
        Create book
        ---
        parameters:
          - in: body
            name: body
            schema:
              type: object
              properties:
                title:
                  type: string
                author:
                  type: string
                status:
                  type: string
                year:
                  type: integer
        responses:
          201:
            description: Book created
        """
        data = request.json
        book = create_book(data)
        return to_dict(book), 201

class BookResource(Resource):
    def get(self, book_id):
        """
        Get a book by ID
        ---
        parameters:
          - name: book_id
            in: path
            type: string
            required: true
        responses:
          200:
            description: Book found
          404:
            description: Not found
        """
        book = get_book(book_id)
        if not book:
            return {"error": "Not found"}, 404
        return to_dict(book)

    def delete(self, book_id):
        """
        Delete a book by ID
        ---
        parameters:
          - name: book_id
            in: path
            type: string
            required: true
        responses:
          204:
            description: Deleted
        """
        remove_book(book_id)
        return "", 204

api.add_resource(BookListResource, "/books")
api.add_resource(BookResource, "/books/<string:book_id>")

if __name__ == "__main__":
    app.run(debug=True, port=5000)