__all__ = ['DataRetriever']

from datetime import datetime
from typing import Optional, Dict, Any

from settings import TWITTER_API_BEARER_TOKEN
from core.clients.twitter.client import TwitterClient
from core.abstract.data_retriever import AbstractDataRetriever
from core.clients.twitter.search_modificators import TweetFieldsEnum, ExpansionsEnum, UserFieldsEnum, PlaceFieldsEnum


class DataRetriever(AbstractDataRetriever):
    @staticmethod
    def _get_raw_data(
        query_string: str,
        start_datetime: datetime,
        end_datetime: datetime
    ) -> Dict[str, Any]:
        tweet_fields: str = ','.join([x.value for x in TweetFieldsEnum])
        expansions: str = ','.join([x.value for x in ExpansionsEnum])
        user_fields: str = ','.join([x.value for x in UserFieldsEnum])
        place_fields: str = ','.join([x.value for x in PlaceFieldsEnum])

        twitter_client = TwitterClient(bearer_token=TWITTER_API_BEARER_TOKEN)
        raw_response = twitter_client.retrieve_tweets(
            query_string=query_string,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            tweet_fields=tweet_fields,
            expansions=expansions,
            user_fields=user_fields,
            place_fields=place_fields
        )
        return raw_response

    def get_mentions(
        self,
        start_datetime: Optional[datetime],
        end_datetime: Optional[datetime]
    ) -> Dict[str, Any]:
        mention = '@FlixBus'
        return self._get_raw_data(
            query_string=mention,
            start_datetime=start_datetime,
            end_datetime=end_datetime
        )
