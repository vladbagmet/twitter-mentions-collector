__all__ = ['AbstractDataRetriever']

from datetime import datetime
from abc import ABC, abstractmethod


class AbstractDataRetriever(ABC):
    @abstractmethod
    def get_tweets(
        self,
        query_string: str,
        start_datetime: datetime,
        end_datetime: datetime,
    ) -> None:
        raise NotImplementedError
