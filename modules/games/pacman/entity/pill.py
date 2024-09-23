import pygame
from game.entity.entity import Entity

class Pill(Entity):
    def __init__(self, *args, power=False, **kwargs):
        super().__init__(*args, **kwargs)
        self._power = power

    def draw(self, surface):
        size = 10 if self._power else 5

        v = pygame.Vector2(self.position.x + 16, self.position.y + 16)
        pygame.draw.circle(surface, "yellow", v, size)