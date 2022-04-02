from app.models.reddit_model import db, RedditData


def get_all_reddit_data():
    return RedditData.query.all()
