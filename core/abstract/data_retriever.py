__all__ = ['AbstractDataRetriever']

from datetime import datetime
from abc import ABC, abstractmethod


class AbstractDataRetriever(ABC):
    @abstractmethod
    def get_mentions(
        self,
        start_datetime: datetime,
        end_datetime: datetime,
    ) -> None:
        raise NotImplementedError
