__all__ = ['AbstractDataProcessor']

from datetime import datetime
from abc import ABC, abstractmethod


class AbstractDataProcessor(ABC):
    @abstractmethod
    def process_tweets(
        self,
        query_string: str,
        start_datetime: datetime,
        end_datetime: datetime,
    ) -> None:
        raise NotImplementedError
