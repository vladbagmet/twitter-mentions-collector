__all__ = ['TweetFieldsEnum', 'ExpansionsEnum', 'UserFieldsEnum', 'PlaceFieldsEnum']

from enum import Enum


class TweetFieldsEnum(str, Enum):
    AUTHOR_ID = 'author_id'
    CREATED_AT = 'created_at'
    ENTITIES = 'entities'
    GEO = 'geo'
    ID = 'id'
    PUBLIC_METRICS = 'public_metrics'
    REFERENCED_TWEETS = 'referenced_tweets'
    SOURCE = 'source'
    TEXT = 'text'
    WITHHELD = 'withheld'


class ExpansionsEnum(str, Enum):
    GEO_PLACE_ID = 'geo.place_id'
    IN_REPLY_TO_USER_ID = 'in_reply_to_user_id'


class UserFieldsEnum(str, Enum):
    CREATED_AT = 'created_at'
    DESCRIPTION = 'description'
    ENTITIES = 'entities'
    ID = 'id'
    LOCATION = 'location'
    PUBLIC_METRICS = 'public_metrics'
    WITHHELD = 'withheld'


class PlaceFieldsEnum(str, Enum):
    COUNTRY = 'country'
    COUNTRY_CODE = 'country_code'
    GEO = 'geo'
    NAME = 'name'
    PLACE_TYPE = 'place_type'
