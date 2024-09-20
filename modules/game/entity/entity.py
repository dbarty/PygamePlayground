import pygame
from pygame import Vector2

class Entity:
    def __init__(self):
        self._position = Vector2()

    def __str__(self) -> str:
        return f"[Entity {type(self).__name__}]"

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position) -> None:
        #assert isinstance(position, Vector2) or None
        if isinstance(position, Vector2):
            position = Vector2()
        self._position = position

    def update(self):
        raise NotImplementedError("The update() method is not implemented, yet!")
        
    def draw(self, screen):
        raise NotImplementedError("The draw() method is not implemented, yet!")