import pygame
from game.entity.entity import Entity

class Wall(Entity):
    def draw(self, surface):
        pygame.draw.rect(surface, "gray", pygame.Rect(*self._position, 32, 32))
