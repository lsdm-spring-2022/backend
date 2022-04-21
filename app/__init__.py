import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from app.routes.data_route import data as data_blueprint

load_dotenv()

db = SQLAlchemy()

USERNAME = os.getenv('MYSQL_USER')
PASSWORD = os.getenv('MYSQL_PASSWORD')
DB_HOST = os.getenv('DATABASE_HOST')
DB_NAME = os.getenv('MYSQL_DATABASE')


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{DB_HOST}/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(data_blueprint)
    db.init_app(app)
    return app
