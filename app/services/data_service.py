import logging
from app.repositories.data_repository import get_all_reddit_data


def get_social_media_data(country, date, source):
    print(
        f'Getting social media data for {country} on {date} from {source}')
    dict = {}
    dict['country'] = country
    dict['date'] = date
    dict['source'] = source
    db_data = get_all_reddit_data()
    return dict
