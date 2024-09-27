import os
import sys

sys.path.insert(0, os.path.abspath('modules'))  # need to find a better solution for this!
#sys.path.append(os.path.abspath('modules'))  # need to find a better solution for this!

from game.game import Game
from games.home.scene.mainmenu import MainMenu
from games.pacman.screen.mazescreen import MazeScene

# Hallo, das ist ein Test

if __name__ == "__main__":
    game = Game()
    game.start(MazeScene())