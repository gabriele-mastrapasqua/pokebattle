from abc import ABC, abstractmethod


class Cacheable(ABC):
    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def set(self, key: str, value: str, ttl : int =None):
        pass

    @abstractmethod
    def delete(self, key: str):
        pass