from flask_restful import Resource, fields, reqparse, marshal_with
from app.models.book import Book
from app import db
import datetime


def validate_year(value):
    try:
        value = int(value)
    except ValueError:
        raise ValueError("Published year must be an integer")

    current_year = datetime.datetime.now().year
    if value < 1000 or value > current_year:
        raise ValueError(f"Published year must be between 1000 and {current_year}")
    return value


def validate_title(value):
    if not isinstance(value, str):
        raise ValueError("Title must be a string")
    if len(value.strip()) == 0:
        raise ValueError("Title cannot be empty")
    if len(value) > 100:
        raise ValueError("Title must be at most 100 characters long")
    return value


def validate_author(value):
    if not isinstance(value, str):
        raise ValueError("Author must be a string")
    if len(value.strip()) == 0:
        raise ValueError("Author cannot be empty")
    if len(value) > 255:
        raise ValueError("Author name must be at most 255 characters")
    return value


book_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'author': fields.String,
    'published_year': fields.Integer,
}
book_parser = reqparse.RequestParser()
book_parser.add_argument('title', type=validate_title, required=True)
book_parser.add_argument('author', type=validate_author, required=True)
book_parser.add_argument('published_year', type=validate_year, required=True)


class BooksResource(Resource):
    @marshal_with(book_fields)
    def get(self):
        books = Book.query.all()
        return books, 200

    @marshal_with(book_fields)
    def post(self):
        args = book_parser.parse_args()
        book = Book(
            title=args['title'],
            author=args['author'],
            published_year=args['published_year']
        )
        db.session.add(book)
        db.session.commit()
        return book, 201


class BookResource(Resource):
    @marshal_with(book_fields)
    def get(self, book_id):
        book = Book.query.get_or_404(book_id)
        return book, 200

    def delete(self, book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return "", 204
