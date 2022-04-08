import logging
from app.repositories.data_repository import get_reddit_data_by_region_and_date
from distutils.util import strtobool


def get_social_media_data(region: str, start_date: str, end_date: str, reddit: str, twitter: str):
    reddit_bool = bool(strtobool(reddit))
    twitter_bool = bool(strtobool(twitter))
    logging.debug(f'Getting social media data for region {region}, start {start_date}, end {end_date}, reddit '
                  f'{reddit_bool}, twitter {twitter_bool}')
    reddit_data = []
    reddit_db_data = None
    if reddit_bool:
        reddit_db_data = get_reddit_data_by_region_and_date(region, start_date, end_date)
    if reddit_db_data is not None:
        for item in reddit_db_data:
            data_dict = {'datePosted': str(item.date_posted), 'region': item.region, 'subreddit': item.subreddit,
                         'postTitle': item.post_title, 'upvotes': item.upvotes, 'dateStored': str(item.date_stored),
                         'comments': item.comments}
            reddit_data.append(data_dict)
    return reddit_data, []
