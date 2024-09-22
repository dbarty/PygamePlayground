from game.entity.entity import Entity
from games.pacman.entity.fruittype import FruitType

class Fruit(Entity):
    def __init__(self, *, type=None):
        super.__init__()
        self._type = type if type else FruitType.random()


