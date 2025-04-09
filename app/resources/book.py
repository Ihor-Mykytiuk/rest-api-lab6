from flask_restful import Resource
from flask import request
from flask_apispec.views import MethodResource
from flask_apispec import use_kwargs, marshal_with
from marshmallow import ValidationError
from app.models.book import Book
from app.schemas.book import BookSchema
from app import db


class BooksResource(MethodResource, Resource):
    @marshal_with(BookSchema(many=True))
    def get(self):
        books = Book.query.all()
        return books, 200

    @use_kwargs(BookSchema, location="json")
    @marshal_with(BookSchema)
    def post(self, data, **kwargs):
        book = data
        db.session.add(book)
        db.session.commit()
        return book, 201


class BookResource(MethodResource, Resource):
    @marshal_with(BookSchema)
    def get(self, book_id):
        book = Book.query.get_or_404(book_id)
        return book, 200

    def delete(self, book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return "", 204
