from app.models.reddit_model import db as reddit_db, RedditModel
from app.models.twitter_model import db as twitter_db, TwitterModel
import logging


def get_reddit_data_by_region_and_date(region: str, start_date: str, end_date: str):
    try:
        reddit_data = RedditModel.query.from_statement(reddit_db.text('SELECT * FROM reddit WHERE region=:region AND date_posted BETWEEN :start AND :end ORDER BY upvotes DESC').params(region=region, start=start_date, end=end_date)).all()
        return reddit_data
    except Exception as e:
        logging.error(e)
        raise Exception(str(e))


def get_twitter_data_by_region_and_date(region: str, start_date: str, end_date: str):
    try:
        twitter_data = TwitterModel.query.from_statement(twitter_db.text('SELECT * FROM twitter WHERE region=:region AND date_posted BETWEEN :start AND :end ORDER BY likes DESC').params(region=region, start=start_date, end=end_date)).all()
        return twitter_data
    except Exception as e:
        logging.error(e)
        raise Exception(str(e))

