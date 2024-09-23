# https://docs.python.org/3/tutorial/modules.html#importing-from-a-package

from game.entity.entity import *
from game.entity.entitygroup import *

__all__ = [
    "entity",
    "entitygroup"
]