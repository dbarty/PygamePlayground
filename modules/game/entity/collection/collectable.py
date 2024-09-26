from abc import ABC, abstractmethod

class Collectable(ABC):
    """This entity can be collected by other entities"""

    @abstractmethod
    def on_collect(self, collector) -> None:
        ...

    def is_collectable(self, collector) -> bool:
        return isinstance(collector, Collector)