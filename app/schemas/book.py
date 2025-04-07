from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models.book import Book


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True

    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    published_year = fields.Str(required=True)
