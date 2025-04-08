from flask_restful import Resource, fields, reqparse, marshal_with
from flask import request
from marshmallow import ValidationError
from app.models.book import Book
from app.schemas.book import BookSchema
from app import db
import datetime

book_schema = BookSchema()
books_schema = BookSchema(many=True)


class BooksResource(Resource):
    def get(self):
        books = Book.query.all()
        return books_schema.dump(books), 200

    def post(self):
        json_data = request.get_json()

        try:
            book = book_schema.load(json_data)
            db.session.add(book)
            db.session.commit()
            return book_schema.dump(book), 201
        except ValidationError as err:
            return {"message": "Validation error", "errors": err.messages}, 400


class BookResource(Resource):
    def get(self, book_id):
        book = Book.query.get_or_404(book_id)
        return book_schema.dump(book), 200

    def delete(self, book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return "", 204
