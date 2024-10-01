from enum import Enum, Flag, auto

class Direction(Enum):
    NEUTRAL = 0
    UP = 1
    DOWN = 2
    LEFT = 4
    RIGHT = 8

class Directions(Flag):
    NEUTRAL = 0
    UP = 1
    DOWN = 2
    LEFT = 4
    RIGHT = 8

