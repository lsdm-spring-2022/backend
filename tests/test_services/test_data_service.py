from app.services.data_service import get_reddit_data, get_twitter_data, get_social_media_data


class TestRedditModel:
    def __init__(self, date_posted, region, subreddit, post_title, upvotes, date_stored, comments):
        self.date_posted = date_posted
        self.region = region
        self.subreddit = subreddit
        self.post_title = post_title
        self.upvotes = upvotes
        self.date_stored = date_stored
        self.comments = comments


test_reddit_data = [
    TestRedditModel('2011-08-23 14:11:09', 'US', 'world', 'test post title 3', 3, '2011-08-23 14:11:09', 30),
    TestRedditModel('2011-08-22 14:11:09', 'US', 'news', 'test post title 2', 2, '2011-08-23 14:11:09', 20),
    TestRedditModel('2011-08-21 14:11:09', 'US', 'worldnews', 'test post title 1', 1, '2011-08-23 14:11:09', 10),
]


class TestTwitterModel:
    def __init__(self, date_posted, region, tweet, likes, retweets, date_stored, comments):
        self.date_posted = date_posted
        self.region = region
        self.tweet = tweet
        self.likes = likes
        self.retweets = retweets
        self.date_stored = date_stored
        self.comments = comments


test_twitter_data = [
    TestTwitterModel('2011-08-23 14:11:09', 'US', 'first test tweet', 3, 30, '2011-08-23 14:11:09', 300),
    TestTwitterModel('2011-08-23 14:11:09', 'US', 'second test tweet', 2, 20, '2011-08-23 14:11:09', 200),
    TestTwitterModel('2011-08-23 14:11:09', 'US', 'third test tweet', 1, 10, '2011-08-23 14:11:09', 100),
]

test_reddit_dict = [
    {
        'comments': 30,
        'datePosted': '2011-08-23 14:11:09',
        'dateStored': '2011-08-21 14:11:09',
        'postTitle': 'test post title 3',
        'region': 'US',
        'subreddit': 'world',
        'upvotes': 3
    },
    {
        'comments': 20,
        'datePosted': '2011-08-22 14:11:09',
        'dateStored': '2011-08-21 14:11:09',
        'postTitle': 'test post title 2',
        'region': 'US',
        'subreddit': 'news',
        'upvotes': 2
    },
    {
        'comments': 0,
        'datePosted': '2011-08-21 14:11:09',
        'dateStored': '2011-08-21 14:11:09',
        'postTitle': 'test post title',
        'region': 'US',
        'subreddit': 'worldnews',
        'upvotes': 1
    }
]


def test_get_reddit_data_no_data(mocker):
    mocker.patch('app.services.data_service.get_reddit_data_by_region_and_date', return_value=[])
    response = get_reddit_data('US', '2022-04-09', '2022-04-10')

    assert response == []


def test_get_reddit_data_exception(mocker):
    mocker.patch('app.services.data_service.get_reddit_data_by_region_and_date',
                 side_effect=Exception('No connection to database'))
    try:
        get_reddit_data('US', '2022-04-09', '2022-04-10')
    except Exception as e:
        assert str(e) == 'No connection to database'


def test_get_reddit_valid_data(mocker):
    mocker.patch('app.services.data_service.get_reddit_data_by_region_and_date', return_value=test_reddit_data)
    response = get_reddit_data('US', '2022-04-09', '2022-04-10')

    assert response == [
        {'datePosted': '2011-08-23 14:11:09', 'region': 'US', 'subreddit': 'world', 'postTitle': 'test post title 3',
         'upvotes': 3, 'dateStored': '2011-08-23 14:11:09', 'comments': 30},
        {'datePosted': '2011-08-22 14:11:09', 'region': 'US', 'subreddit': 'news', 'postTitle': 'test post title 2',
         'upvotes': 2, 'dateStored': '2011-08-23 14:11:09', 'comments': 20},
        {'datePosted': '2011-08-21 14:11:09', 'region': 'US', 'subreddit': 'worldnews',
         'postTitle': 'test post title 1', 'upvotes': 1, 'dateStored': '2011-08-23 14:11:09', 'comments': 10}]


def test_get_twitter_data_no_data(mocker):
    mocker.patch('app.services.data_service.get_twitter_data_by_region_and_date', return_value=[])
    response = get_twitter_data('US', '2022-04-09', '2022-04-10')

    assert response == []


def test_get_twitter_data_exception(mocker):
    mocker.patch('app.services.data_service.get_twitter_data_by_region_and_date',
                 side_effect=Exception('No connection to database'))
    try:
        get_twitter_data('US', '2022-04-09', '2022-04-10')
    except Exception as e:
        assert str(e) == 'No connection to database'


def test_get_twitter_valid_data(mocker):
    mocker.patch('app.services.data_service.get_twitter_data_by_region_and_date', return_value=test_twitter_data)
    response = get_twitter_data('US', '2022-04-09', '2022-04-10')

    assert response == [
        {'datePosted': '2011-08-23 14:11:09', 'region': 'US', 'tweet': 'first test tweet', 'likes': 3, 'retweets': 30,
         'dateStored': '2011-08-23 14:11:09', 'comments': 300},
        {'datePosted': '2011-08-23 14:11:09', 'region': 'US', 'tweet': 'second test tweet', 'likes': 2, 'retweets': 20,
         'dateStored': '2011-08-23 14:11:09', 'comments': 200},
        {'datePosted': '2011-08-23 14:11:09', 'region': 'US', 'tweet': 'third test tweet', 'likes': 1, 'retweets': 10,
         'dateStored': '2011-08-23 14:11:09', 'comments': 100}]


def test_get_social_media_data_no_data(mocker):
    mocker.patch('app.services.data_service.get_reddit_data', return_value=[])
    mocker.patch('app.services.data_service.get_twitter_data', return_value=[])
    response = get_social_media_data('US', '2011-08-20', '2011-08-25', 'true', 'true')

    assert response == ([], [])


def test_get_social_media_data_exception(mocker):
    mocker.patch('app.services.data_service.get_reddit_data', side_effect=Exception('No connection to database'))
    mocker.patch('app.services.data_service.get_twitter_data', side_effect=Exception('No connection to database'))
    try:
        get_social_media_data('US', '2011-08-20', '2011-08-25', 'true', 'true')
    except Exception as e:
        assert str(e) == 'No connection to database'


def test_get_social_media_data_valid_data(mocker):
    mocker.patch('app.services.data_service.get_reddit_data', return_value=test_reddit_dict)
    mocker.patch('app.services.data_service.get_twitter_data', return_value=[])
    response = get_social_media_data('US', '2011-08-20', '2011-08-25', 'true', 'true')

    assert response == (test_reddit_dict, [])
