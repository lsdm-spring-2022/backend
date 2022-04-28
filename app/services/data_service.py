import logging
from app.repositories.data_repository import get_reddit_data_by_region_and_date, get_twitter_data_by_region_and_date
from distutils.util import strtobool


def get_social_media_data(region: str, start_date: str, end_date: str, reddit: str, twitter: str, limit: str):
    reddit_bool = bool(strtobool(reddit))
    twitter_bool = bool(strtobool(twitter))
    limit_num = int(limit)
    logging.debug(f'Getting social media data for region {region}, start {start_date}, end {end_date}, reddit '
                  f'{reddit_bool}, twitter {twitter_bool}')
    reddit_data = []
    twitter_data = []
    try:
        if reddit_bool:
            reddit_data = get_reddit_data(
                region, start_date, end_date, limit_num)
        if twitter_bool:
            twitter_data = get_twitter_data(
                region, start_date, end_date, limit_num)
        return reddit_data, twitter_data
    except Exception as e:
        logging.error(e)
        raise Exception(str(e))


def get_reddit_data(region: str, start_date: str, end_date: str, limit: int):
    try:
        reddit_data = []
        db_data = get_reddit_data_by_region_and_date(
            region, start_date, end_date, limit)
        if db_data is not None:
            for item in db_data:
                data_dict = {'datePosted': str(item.date_posted), 'region': item.region, 'subreddit': item.subreddit,
                             'postTitle': item.post_title, 'upvotes': item.upvotes, 'dateStored': str(item.date_stored),
                             'comments': item.comments}
                reddit_data.append(data_dict)
        return reddit_data
    except Exception as e:
        logging.error(e)
        raise Exception(str(e))


def get_twitter_data(region: str, start_date: str, end_date: str, limit: int):
    try:
        twitter_data = []
        db_data = get_twitter_data_by_region_and_date(
            region, start_date, end_date, limit)
        if db_data is not None:
            for item in db_data:
                data_dict = {'dateTrendStarted': str(item.created_at), 'region': item.country, 'trend': item.trend,
                             'tweetVolume': item.tweet_volume, 'dateRetrieved': str(item.as_of)}
                twitter_data.append(data_dict)
        return twitter_data
    except Exception as e:
        logging.error(e)
        raise Exception(str(e))
