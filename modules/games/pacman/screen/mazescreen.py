import os
from game.scene.scene import Scene
from game.entity.entitygroup import EntityGroup
from games.pacman.mazeloader import MazeLoader
from games.pacman.entity.player import Player

class MazeScene(Scene):
    def __init__(self):
        super().__init__()

        loader = MazeLoader()
        self._entities =loader.load(os.path.abspath('modules/games/pacman/data/levels/level1.txt'))

        player = Player()
        player.moveTo(14*32, 14*32)

        self._entities.add(player)

    def animate(self, game):
        self._entities.draw(game.display.surface)