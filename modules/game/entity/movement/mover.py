from abc import ABC, abstractmethod

class Mover(ABC):
    """This entity is able to move others"""

    @abstractmethod
    def can_move(self, other) -> bool:
        """Returns a boolean whether this entiy can move another or not"""
        ...