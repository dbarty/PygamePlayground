import random
from enum import Enum, auto

class FruitType(Enum):
    APPLE = auto()
    BANANA = auto()
    CHERRY = auto()
    LEMON = auto()
    MELON = auto()
    ORANGE = auto()
    PEAR = auto()
    PEACH = auto()
    STRAWBERRY = auto()

    @classmethod
    def random(cls):
        # Maybe it isn't that nice, but it seems to work
        return random.choice(list(cls.__members__.values()))