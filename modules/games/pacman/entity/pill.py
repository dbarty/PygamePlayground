import pygame
from game.entity.entity import Entity

class Pill(Entity):
    def draw(self, surface):
        pygame.draw.circle(surface, "yellow", self.position, 10)