from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TwitterModel(db.Model):
    __tablename__ = 'twitter'
    date_posted = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(50))
    tweet = db.Column(db.String(280), primary_key=True)
    likes = db.Column(db.Integer)
    retweets = db.Column(db.Integer)
    date_stored = db.Column(db.String(45))
    comments = db.Column(db.Integer)