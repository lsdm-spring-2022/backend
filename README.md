# Backend
Backend repository

## Local Development
1. Ensure that you have either connected to the database or setup a local database
2. Create a `.env` file using the structure defined in the `.env.sample` file
3. Setup virtual environment using something like Pipenv or venv
4. Run the `app.py` file in the project root to start the application

### Social Media Data Endpoint
When the application is run locally, the endpoint is available at `http://localhost:5001/api/data`. The endpoint expects and validates that the following query parameters are present in the GET request:
```
region: A string representing a region (e.g., 'US')
startDate: A date string in the YYYY-MM-DD format (e.g., '2011-08-20')
endDate: A date string in the YYYY-MM-DD format (e.g., '2011-08-21')
reddit: A boolean string (e.g., 'true')
twitter: A boolean string (e.g., 'false')
```

If there are no errors, the endpoint response will look like:
```json
{
    "reddit": [
        {
            "comments": 30,
            "datePosted": "2011-08-23 14:11:09",
            "dateStored": "2011-08-21 14:11:09",
            "postTitle": "test post title 3",
            "region": "US",
            "subreddit": "world",
            "upvotes": 3
        },
        {
            "comments": 20,
            "datePosted": "2011-08-22 14:11:09",
            "dateStored": "2011-08-21 14:11:09",
            "postTitle": "test post title 2",
            "region": "US",
            "subreddit": "news",
            "upvotes": 2
        },
        {
            "comments": 0,
            "datePosted": "2011-08-21 14:11:09",
            "dateStored": "2011-08-21 14:11:09",
            "postTitle": "test post title",
            "region": "US",
            "subreddit": "worldnews",
            "upvotes": 1
        }
    ],
    "twitter": []
}
```

If an error occurs, the endpoint response will look like:
```json
{
    "message": "(pymysql.err.OperationalError) (2003, \"Can't connect to MySQL server on '0.0.0.0' ([Errno 61] Connection refused)\")\n(Background on this error at: https://sqlalche.me/e/14/e3q8)"
}
```