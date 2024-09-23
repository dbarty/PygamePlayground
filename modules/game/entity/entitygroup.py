from pygame import Vector2
from game.entity.entity import Entity

class EntityGroup:
    def __init__(self, gridstep=32) -> None:
        self._items: list = []
        self._gridstep = gridstep

    def __str__(self) -> str:
        return f"[EntityGroup items={len(self)}]"

    def __len__(self) -> int:
        return len(self._items)
    
    def add(self, entity: Entity):
        assert isinstance(entity, Entity)
        self._items.append(entity)

    def addXY(self, x, y, entity:Entity) -> None:
        entity.moveTo(x * self._gridstep, y * self._gridstep)
        self.add(entity)

    def update(self, *args, **kwargs) -> None:
        for entity in self._items:
            entity.update(*args, **kwargs)

    def draw(self, *args, **kwargs) -> None:
        for entity in self._items:
            entity.draw(*args, **kwargs)