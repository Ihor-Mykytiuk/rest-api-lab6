from flask_restful import Resource, fields, reqparse, marshal_with
from app.models.book import Book
from app import db

book_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'author': fields.String,
    'published_year': fields.String,
}
book_parser = reqparse.RequestParser()
book_parser.add_argument('title', type=str, required=True)
book_parser.add_argument('author', type=str, required=True)
book_parser.add_argument('published_year', type=str, required=True)


class BooksResource(Resource):
    @marshal_with(book_fields)
    def get(self):
        books = Book.query.all()
        return books, 200

    @marshal_with(book_fields)
    def post(self):
        args = book_parser.parse_args()
        title = args['title']
        author = args['author']
        published_year = args['published_year']
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
