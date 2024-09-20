import pygame
import pygame_menu
from pygame_menu import themes
from game.scene.menuscene import MenuScene

class MainMenu(MenuScene):
    def __init__(self):
        self._menu = pygame_menu.Menu('PyGame Playground', 800, 600, theme=themes.THEME_DARK)
        self._menu.add.button('Quit', self.quit)

    def quit(self):
        pygame.quit()