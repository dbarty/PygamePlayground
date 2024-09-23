import pygame
from game.entity.entity import Entity

class Player(Entity):
    def draw(self, surface):
        rect = pygame.Rect(self.position.x, self.position.y, 32, 32)
        pygame.draw.arc(surface, "yellow", rect, 30, 50)

