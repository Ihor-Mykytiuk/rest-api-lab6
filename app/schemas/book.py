from app.models.book import Book
from app import ma


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
    id = ma.auto_field()
    title = ma.auto_field()
    author = ma.auto_field()
    published_year = ma.auto_field()
