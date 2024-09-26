import pygame
from game.entity import Entity
from games.pacman.entity.ghosttype import GhostType

class Ghost(Entity):
    def __init__(self, *args, type=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._type = type if type else GhostType.random()
    
    def __str__(self) -> str:
        return f"[Entity Ghost ({self._type.name})]"
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        self._type = type

    def draw(self, surface):
        # https://www.pygame.org/docs/ref/color_list.html

        color = self.type.value


        pygame.draw.rect(surface, color, pygame.Rect(self.position.x + 5, self.position.y + 5, 22, 22))