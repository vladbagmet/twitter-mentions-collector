__all__ = ['AbstractTwitterClient']

from datetime import datetime
from typing import Optional
from abc import ABC, abstractmethod


class AbstractTwitterClient(ABC):
    @abstractmethod
    def retrieve_tweets(
        self,
        query_string: str,
        start_datetime: datetime,
        end_datetime: datetime,
        tweet_fields: Optional[str],
        expansions: Optional[str],
        user_fields: Optional[str],
        place_fields: Optional[str]
    ) -> None:
        raise NotImplementedError
