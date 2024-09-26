from game.entity import Entity

class EntityGroup:
    def __init__(self, gridstep=32) -> None:
        self._items: list = []
        self._gridstep = gridstep

    def __str__(self) -> str:
        return f"[EntityGroup items={len(self)}]"

    def __len__(self) -> int:
        return len(self._items)
    
    def add(self, entity: Entity):
        "Add an entity to that group"
        assert isinstance(entity, Entity)
        self._items.append(entity)

    def addXY(self, x, y, entity:Entity) -> None:
        "Add an entity to that group with a by x&y calculated grid position"
        entity.moveTo(x * self._gridstep, y * self._gridstep)
        self.add(entity)

    def pairs(self):
        """
        This is a generator to loop in a more efficient way over all entities and
        yields a tuple with two entities
        """
        for i in range(len(self._items)):
            for ii in range(i+1, len(self._items)):
                yield (self._items[i], self._items[ii])

    def update(self, *args, **kwargs) -> None:
        for entity in self._items:
            entity.update(*args, **kwargs)

    def draw(self, *args, **kwargs) -> None:
        for entity in self._items:
            entity.draw(*args, **kwargs)