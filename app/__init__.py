from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow
from flask_apispec import FlaskApiSpec

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
ma = Marshmallow()
docs = FlaskApiSpec()

def create_app(config_name='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)
    ma.init_app(app)
    from app.models.book import Book
    with app.app_context():
        db.create_all()

    api = Api(app, prefix='/api/v1')
    from app.resources.book import BookResource
    from app.resources.book import BooksResource
    api.add_resource(BooksResource, '/books')
    api.add_resource(BookResource, '/books/<int:book_id>')

    docs.init_app(app)
    docs.register(BookResource)
    docs.register(BooksResource)
    return app
