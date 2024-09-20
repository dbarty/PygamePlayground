import os
from game.scene.scene import Scene
from game.entity.entitygroup import EntityGroup
from games.pacman.mazeloader import MazeLoader

class MazeScene(Scene):
    def __init__(self):
        super().__init__()

        self._entities = EntityGroup()

        loader = MazeLoader()
        entities = loader.load(os.path.abspath('modules/games/pacman/data/levels/level1.txt'))

        for line in entities:
            for entity in line:
                self._entities.add(entity)

    def animate(self, game):
        self._entities.draw(game.display.surface)



