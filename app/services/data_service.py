import logging
from app.repositories.data_repository import get_reddit_data_by_region_and_date
from distutils.util import strtobool


def get_social_media_data(region: str, start_date: str, end_date: str, reddit: str, twitter: str):
    reddit_bool = bool(strtobool(reddit))
    twitter_bool = bool(strtobool(twitter))
    logging.debug(f'Getting social media data for region {region}, start {start_date}, end {end_date}, reddit '
                  f'{reddit_bool}, twitter {twitter_bool}')
    reddit_data = []
    twitter_data = []
    if reddit_bool:
        reddit_data = get_reddit_data(region, start_date, end_date)
    if twitter_bool:
        twitter_data = get_twitter_data(region, start_date, end_date)
    return reddit_data, twitter_data


def get_reddit_data(region: str, start_date: str, end_date: str):
    reddit_data = []
    db_data = get_reddit_data_by_region_and_date(region, start_date, end_date)
    if db_data is not None:
        for item in db_data:
            data_dict = {'datePosted': str(item.date_posted), 'region': item.region, 'subreddit': item.subreddit,
                         'postTitle': item.post_title, 'upvotes': item.upvotes, 'dateStored': str(item.date_stored),
                         'comments': item.comments}
            reddit_data.append(data_dict)
    return reddit_data


def get_twitter_data(region: str, start_date: str, end_date: str):
    twitter_data = []
    db_data = []
    if db_data is not None:
        twitter_data = []
    return twitter_data