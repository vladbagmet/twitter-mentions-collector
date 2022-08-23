__all__ = ['AbstractStorage']

from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def set(self, *args, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, *args, **kwargs) -> None:
        raise NotImplementedError
