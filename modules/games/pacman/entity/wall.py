import pygame
from game.entity import Entity
from game.entity.collision.collidable import Collidable

class Wall(Entity, Collidable):

    def on_collision(self, other):
        ...

    def get_colliders(self):
        ...
        
    def draw(self, surface):
        pygame.draw.rect(surface, "gray", pygame.Rect(*self._position, 32, 32))
