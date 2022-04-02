import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from app.routes.data import data as data_blueprint

load_dotenv()

db = SQLAlchemy()

USERNAME = os.getenv('DATABASE_USERNAME')
PASSWORD = os.getenv('DATABASE_PASSWORD')
DB_URI = os.getenv('DATABASE_URI')
DB_NAME = os.getenv('DATABASE_NAME')


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{DB_URI}/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(data_blueprint)
    db.init_app(app)
    return app
