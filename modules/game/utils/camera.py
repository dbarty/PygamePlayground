from game.entity.entity import Entity

class Camera:    
    def __init__(self, playground, entity=None):
        self._playground = playground
        self._entity = entity
    
    def __str__(self):
        return f"[Camera entity={self.entity}]"

    @property
    def entity(self):
        return self._entity
    
    @entity.setter
    def entity(self, entity):
        assert isinstance(entity, Entity)
        self._entity = entity

    @property
    def playground(self):
        return self._playground