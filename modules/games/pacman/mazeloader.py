import pygame
from game.entity.entitygroup import EntityGroup
from games.pacman.entity.pill import Pill
from games.pacman.entity.wall import Wall

class MazeLoader:
    def load(self, filename):
        entities = EntityGroup()

        # maybe outsource this double loop into an reuseable iterator
        with open(filename) as file:
            for y, line in enumerate(file.readlines()):
                for x, char in enumerate(line):
                    entity = self._createEntity(char)

                    if entity:
                        entities.addXY(x, y, entity)

        return entities
    
    def _createEntity(self, char):
        entity = None

        if char == "#":
            entity = Wall()
        elif char == ".":
            entity = Pill()
        elif char == "*":
            entity = Pill(power=True)

        return entity

