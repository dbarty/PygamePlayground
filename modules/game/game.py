from game.scene.scene import Scene
from game.utils.display import Display
from game.utils.gameloop import GameLoop

class Game:
    def __init__(self, display:Display=None, *, scene:Scene=None, loop:GameLoop=None) -> None:
        self._display = display if display else Display()  # set a default display
        self._loop = loop if loop else GameLoop()  # set a default loop
        self._scene = scene if scene else Scene()  # set a default scene

    @property
    def display(self):
        return self._display
    
    @property
    def loop(self) -> GameLoop:
        return self._loop
    
    @property
    def scene(self) -> Scene:
        return self._scene
    
    @scene.setter
    def scene(self, scene:Scene):
        self._scene = scene
    
    def start(self, scene:Scene=None):
        self.scene = scene
        self._loop.start(self.animate)

    def stop(self) -> None:
        self._loop.stop()

    def animate(self, loop:GameLoop):
        self._display.beforeLoop()
        self._scene.animate(self)
        self._display.afterLoop()