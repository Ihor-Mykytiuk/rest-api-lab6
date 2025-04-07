from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase



class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def create_app(config_name='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)
    from app.models.book import Book
    with app.app_context():
        db.create_all()

    api = Api(app)
    from app.resources.book import BookResource
    from app.resources.book import BooksResource
    api.add_resource(BooksResource, '/api/v1/books')
    api.add_resource(BookResource, '/api/v1/books/<int:book_id>')
    return app
