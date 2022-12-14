import os

MAX_DAYS_BACK_DATA_RETRIEVAL_ALLOWED = 7  # Only tweets for last week can be retrieved.

TWITTER_API_BEARER_TOKEN = os.getenv('TWITTER_API_BEARER_TOKEN')

AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')
DYNAMODB_TABLE_NAME = os.getenv('DYNAMODB_TABLE_NAME')
