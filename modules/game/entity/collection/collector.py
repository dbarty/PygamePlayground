from abc import ABC, abstractmethod
from game.entity.collection.collectable import Collectable

class Collector(ABC):
    """This entity can collect others"""

    @abstractmethod
    def collect(self, collectable:Collectable) -> None:
        """The entity collects another"""
        ...

    def can_collect(self, collectable:Collectable) -> bool:
        """Returns a boolean whether this entity can collect another or not"""
        return isinstance(collectable, Collectable)