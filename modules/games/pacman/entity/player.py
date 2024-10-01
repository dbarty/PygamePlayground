import pygame
from game.game import Game
from game.entity import Entity
from game.entity.collision.collidable import Collidable
from game.entity.collection.collector import Collector
from game.entity.collection.collectable import Collectable
from game.utils.direction import Direction, Directions

class Player(Entity, Collidable, Collector):
    def __init__(self) -> None:
        super().__init__()
        self.zindex = 127
        self._direction = Direction(value=0)
        self._speed = 3

    @property
    def direction(self) -> Direction:
        return self._direction
    
    def on_collision(self, other):
        ...

    def get_colliders(self):
        ...

    def collect(self, collectable:Collectable) -> None:
        ...

    def update(self, game:Game):
        xi, yi = self.grid.pos_to_index(self.position)

        print("update()", self.grid, (xi, yi), self.grid.get(xi, yi)
)

        # -----
        self._set_direction_by_keys(pygame.key.get_pressed(), self.grid.get(xi, yi))
        self._calculate_position()
        
    def draw(self, surface) -> None:
        rect = pygame.Rect(self.position.x+1, self.position.y+1, 30, 30)
        pygame.draw.arc(surface, "yellow", rect, 30, 50)

    def _set_direction_by_keys(self, keys, ds):
        if not isinstance(ds, Directions):
            self._direction = Direction.NEUTRAL
            return

        if Directions.LEFT in ds and keys[pygame.K_LEFT]:
            self._direction = Direction.LEFT
        if Directions.RIGHT in ds and keys[pygame.K_RIGHT]:
            self._direction = Direction.RIGHT
        if Directions.UP in ds and keys[pygame.K_UP]:
           self._direction = Direction.UP
        if Directions.DOWN in ds and keys[pygame.K_DOWN]:
            self._direction = Direction.DOWN

    def _calculate_position(self):
        match self._direction:
            case Direction.LEFT:
                self.position.x -= self._speed
            case Direction.RIGHT:
                self.position.x += self._speed
            case Direction.UP:
                self.position.y -= self._speed
            case Direction.DOWN:
                self.position.y += self._speed
            case Direction.NEUTRAL:
                x, y = self.grid.clean_position(self.position.x + 16, self.position.y + 16)  # Add half size. Need a better solution
                self.position.x = x
                self.position.y = y