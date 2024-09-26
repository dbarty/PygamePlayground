from game.entity import EntityGroup
from game.entity.collision.collidable import Collidable
from game.entity.collection.collector import Collector
from game.entity.collection.collectable import Collectable

class EntityManager:
    def __init__(self, group:EntityGroup):
        self._group = group

    def animate(self, game):  # maybe change the methodname later
        #col = 0
        # - loop over all entities
        for entity1, entity2 in self._group.pairs():
            ...
            # check collision
            #if isinstance(entity1, Collidable) and isinstance(entity2, Collidable):
            #    collision = self._check_collision(entity1, entity2)

            # check, if the entity can collect the other
            #if isinstance(entity1, Collector) or isinstance(entity2, Collectable):
            #    col += 1

        # - manage movement and collisions
        # - collect and consume items
        # - update items to get their desired movement
        # - 


        #print(col)

    def _check_collision(self, entity1, entity2):
        return False  # Sure, we need more magic here... ;-)