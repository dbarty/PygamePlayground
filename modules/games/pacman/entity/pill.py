import pygame
from game.entity.entity import Entity

class Pill(Entity):
    def draw(self, surface):
        v = pygame.Vector2(self.position.x + 16, self.position.y + 16)
        pygame.draw.circle(surface, "yellow", v, 5)