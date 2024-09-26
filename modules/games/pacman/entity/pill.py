import pygame
from game.entity import Entity
from game.entity.collection.collectable import Collectable

class Pill(Entity, Collectable):
    def __init__(self, *args, power=False, **kwargs):
        super().__init__(*args, **kwargs)
        self._power = power

    def on_collect(self, collector) -> None:
        ...

    def draw(self, surface):
        size = 10 if self._power else 5

        v = pygame.Vector2(self.position.x + 16, self.position.y + 16)
        pygame.draw.circle(surface, "yellow", v, size)