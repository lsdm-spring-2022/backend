from app.models.reddit_model import db, RedditData
import logging


def get_reddit_data_by_region_and_date(region: str, start_date: str, end_date: str):
    try:
        reddit_data = RedditData.query.from_statement(db.text('SELECT * FROM reddit WHERE region=:region AND date_posted BETWEEN :start AND :end').params(region=region, start=start_date, end=end_date)).all()
        return reddit_data
    except Exception as e:
        logging.error(e)
        return None
