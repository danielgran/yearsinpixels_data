from abc import ABC, abstractmethod

from yearsinpixels_business.Entity.Entity import Entity


class Gateway(ABC):
    @abstractmethod
    def create_entity(self, entity):
        pass

    @abstractmethod
    def read_entity(self, entity) -> Entity:
        pass

    @abstractmethod
    def update_entity(self, entity):
        pass

    @abstractmethod
    def delete_entity(self, entity):
        pass
