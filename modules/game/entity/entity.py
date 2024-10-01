import pygame
from pygame import Vector2
from game.game import Game

class Entity:
    def __init__(self, *, position=None):
        self._position = position if position else Vector2()
        self._layer = 0
        self._zindex = 0

    def __str__(self) -> str:
        return f"[Entity {type(self).__name__}]"

    def __repr__(self) -> str:
        return self.__str__()
    
    @property
    def position(self):
        return self._position

    @property
    def layer(self) -> int:
        return self._layer
    
    @layer.setter
    def layer(self, layer:int) -> None:
        self._layer = layer

    @property
    def zindex(self) -> int:
        return self._zindex
    
    @zindex.setter
    def zindex(self, zindex) -> None:
        self._zindex = zindex

    @position.setter
    def position(self, position) -> None:
        #assert isinstance(position, Vector2) or None
        #if isinstance(position, Vector2):
        #position = Vector2()
        self._position = position

    def moveTo(self, x, y) -> None:
        self.position.x = x
        self.position.y = y

    def update(self, game:Game):
        ... # raise NotImplementedError("The update() method is not implemented, yet!")
        
    def draw(self, screen):
        ... # raise NotImplementedError("The draw() method is not implemented, yet!")