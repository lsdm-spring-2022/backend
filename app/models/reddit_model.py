from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class RedditModel(db.Model):
    __tablename__ = 'reddit'
    date_posted = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(50))
    subreddit = db.Column(db.String(20), primary_key=True)
    post_title = db.Column(db.String(255))
    upvotes = db.Column(db.Integer)
    date_stored = db.Column(db.String(45))
    comments = db.Column(db.Integer)
