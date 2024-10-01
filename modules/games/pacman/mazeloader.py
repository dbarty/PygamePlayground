import pygame
from game.entity.entitygroup import EntityGroup
from games.pacman.entity.pill import Pill
from games.pacman.entity.wall import Wall
from games.pacman.utils.grid import Grid

class MazeLoader:
    def load(self, filename):
        entities = EntityGroup()
        grid = Grid()

        # maybe outsource this double loop into an reuseable iterator
        with open(filename) as file:
            for y, line in enumerate(file.readlines()):
                for x, char in enumerate(line):
                    entity = self._createEntity(char)

                    if entity:
                        entities.addXY(x, y, entity)
                        grid.addXY(x, y, entity)
            grid.update()

        return (entities, grid)
    
    def _createEntity(self, char):
        entity = None

        if char == "#":
            entity = Wall()
        elif char == ".":
            entity = Pill()
        elif char == "*":
            entity = Pill(power=True)

        return entity

