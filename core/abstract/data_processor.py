__all__ = ['AbstractDataProcessor']

from datetime import datetime
from abc import ABC, abstractmethod


class AbstractDataProcessor(ABC):
    @abstractmethod
    def process_mentions(
        self,
        start_datetime: datetime,
        end_datetime: datetime,
    ) -> None:
        raise NotImplementedError
