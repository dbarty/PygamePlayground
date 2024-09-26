import pygame
from game.game import Game
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

    def update(self, game:Game):

        # calculate new position
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.position.x -= 5 
        if keys[pygame.K_RIGHT]:
            self.position.x += 5
        if keys[pygame.K_UP]:
           self.position.y -= 5  
        if keys[pygame.K_DOWN]:
            self.position.y += 5 

    def draw(self, surface) -> None:
        rect = pygame.Rect(self.position.x+1, self.position.y+1, 30, 30)
        pygame.draw.arc(surface, "yellow", rect, 30, 50)

