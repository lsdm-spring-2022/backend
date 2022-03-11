from flask import Flask

from app.routes.data import data as data_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(data_blueprint)
    return app
