from abc import ABC, abstractmethod

class Collidable(ABC):
    
    @abstractmethod
    def on_collision(self, other):
        ...

    @abstractmethod
    def get_colliders(self):
        ...
