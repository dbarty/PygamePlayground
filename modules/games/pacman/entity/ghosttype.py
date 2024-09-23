import random
from enum import Enum, auto

class GhostType(Enum):
    BLINKY = "red"
    PINKY = "pink"
    INKY = "cyan"
    CLYDE = "orange"

    @classmethod
    def random(cls):
        # Maybe it isn't that nice, but it seems to work
        return random.choice(list(cls.__members__.values()))