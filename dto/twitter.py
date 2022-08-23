__all__ = ['Tweets']

from typing import Optional, List

from pydantic import BaseModel


class HashTag(BaseModel):
    text: Optional[str]


class User(BaseModel):
    id: int
    followers_count: int
    statuses_count: int


class TweetEntities(BaseModel):
    hashtags: List[HashTag]


class Tweet(BaseModel):
    created_at: str
    id: int
    text: str
    entities: TweetEntities
    user: User
    coordinates: Optional[str]
    retweeted: bool


class Tweets(BaseModel):
    statuses: List[Tweet]
