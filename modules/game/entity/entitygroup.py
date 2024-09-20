from game.entity.entity import Entity

class EntityGroup:
    def __init__(self) -> None:
        self._items: list = []

    def __str__(self) -> str:
        return f"[EntityGroup items={len(self)}]"

    def __len__(self) -> int:
        return len(self._items)
    
    def add(self, entity: Entity):
        assert isinstance(entity, Entity)
        self._items.append(entity)

    def update(self, *args, **kwargs) -> None:
        for entity in self._items:
            entity.update(*args, **kwargs)

    def draw(self, *args, **kwargs) -> None:
        for entity in self._items:
            entity.draw(*args, **kwargs) 