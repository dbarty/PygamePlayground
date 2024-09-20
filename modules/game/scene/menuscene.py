import pygame
import pygame_menu
from game.scene.scene import Scene

class MenuScene(Scene):
    def __init__(self):
        self._menu = None

    def animate(self, game):
        super().animate(game)

        events = pygame.event.get()

        #if self._menu.is_enabled():
        self._menu.update(events)
        self._menu.draw(game.display.surface)