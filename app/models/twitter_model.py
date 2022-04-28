from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TwitterModel(db.Model):
    __tablename__ = 'twitter'
    country = db.Column(db.String(50), primary_key=True)
    created_at = db.Column(db.String)
    trend = db.Column(db.String(100), primary_key=True)
    tweet_volume = db.Column(db.Integer)
    as_of = db.Column(db.String)
