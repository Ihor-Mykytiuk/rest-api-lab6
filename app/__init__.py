from flask import Flask
from flask_restful import Api
from app.resources.book import BookResource


def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(BookResource, '/book')
    return app
