import pygame

class GameLoop:
    def __init__(self, loop_breaker=None):
        self._loop_breaker = loop_breaker if loop_breaker else self._loop_breaker_fn
        self._clock = pygame.time.Clock()
        self._running = False
        self._dt = 0
    
    def start(self, fn):
        self._running = True
        self._loop(fn)

    def stop(self):
        self._running = False

    def is_running(self):
        return self._running
        
    def _loop(self, fn):
        while self._running:
            try:
                self._loop_breaker()

                fn(self)
                self._dt = self._clock.tick(60) / 1000
            except Exception as ex:
                print("Game over due to an error!", ex)
                self.stop()
                pygame.quit()

    def _loop_breaker_fn(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.stop()

    @property
    def dt(self) -> float:
        return self._dt