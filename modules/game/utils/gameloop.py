import pygame

class GameLoop:
    def __init__(self, fps=60, loop_breaker=None):
        self._frames = fps
        self._loop_breaker = loop_breaker if loop_breaker else self._loop_breaker_fn
        self._clock = pygame.time.Clock()
        self._running = False
        self._dt = 0
    
    @property
    def running(self) -> bool:
        return self._running
    
    @property
    def fps(self) -> int:
        return int(self._clock.get_fps())

    @property
    def dt(self) -> float:
        return self._dt

    def start(self, fn):
        "Start the GameLoop"
        self._running = True
        self._loop(fn)

    def stop(self):
        "Stop the GameLoop"
        self._running = False

    def _loop(self, fn):
        while self._running:
            try:
                self._loop_breaker()

                fn(self)
                self._dt = self._clock.tick(self._frames) / 1000
            except Exception as ex:
                print("Game over due to an error!", ex)
                self.stop()
                pygame.quit()

    def _loop_breaker_fn(self):
        i=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.stop()
            i += 1
        #print("event count: ", i)