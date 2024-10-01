import os
from game.entity import EntityManager
from game.scene.scene import Scene
from games.pacman.mazeloader import MazeLoader
from games.pacman.entity.player import Player
from games.pacman.entity.ghost import Ghost

class MazeScene(Scene):
    def __init__(self):
        super().__init__()

        loader = MazeLoader()
        self._entities, self._grid = loader.load(os.path.abspath('modules/games/pacman/data/levels/level1.txt'))

        #print(self._grid, self._grid.get(1,1))

        player = Player()
        player.moveTo(14*32, 14*32)
        player.grid = self._grid  # Only temp to try...

        self._entities.add(player)

        # Note: We need a ghost factory...
        ghost = Ghost()
        ghost.moveTo(12*32, 12*32)
        self._entities.add(ghost)

        ghost = Ghost()
        ghost.moveTo(13*32, 12*32)
        self._entities.add(ghost)

        ghost = Ghost()
        ghost.moveTo(14*32, 12*32)
        self._entities.add(ghost)

        ghost = Ghost()
        ghost.moveTo(15*32, 12*32)
        self._entities.add(ghost)

        #self._manager = EntityManager(self._entities)

    def animate(self, game):
        #self._manager.animate(game)

        self._entities.update(game)
        self._entities.draw(game.display.surface)