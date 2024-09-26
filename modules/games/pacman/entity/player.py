import pygame
from game.entity import Entity
from game.entity.collision.collidable import Collidable
from game.entity.collection.collector import Collector
from game.entity.collection.collectable import Collectable

class Player(Entity, Collidable, Collector):

    def on_collision(self, other):
        ...

    def get_colliders(self):
        ...

    def collect(self, collectable:Collectable) -> None:
        ...

    def draw(self, surface) -> None:
        rect = pygame.Rect(self.position.x, self.position.y, 32, 32)
        pygame.draw.arc(surface, "yellow", rect, 30, 50)

