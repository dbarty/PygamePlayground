import pygame

class Display:
    def __init__(self, size:tuple=(1024, 1000), *, caption=None) -> None:
        pygame.init()  # Not sure, if there could be a better place, but good for now...

        if caption:
            pygame.display.set_caption(caption)

        self._size = size
        self._surface = pygame.display.set_mode(self._size)

    @property
    def size(self):
        return self._size
    
    @property
    def surface(self):
        return self._surface
    
    def beforeLoop(self):
        ...

    def afterLoop(self):
        pygame.display.flip()