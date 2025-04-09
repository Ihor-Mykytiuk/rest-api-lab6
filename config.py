import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APISPEC_TITLE = "Books API"
    APISPEC_VERSION = "v1"
    APISPEC_SWAGGER_URL = "/swagger/"
    APISPEC_SWAGGER_UI_URL = "/docs/"