from abc import ABC, abstractmethod

from yearsinpixels_business.Entity.Entity import Entity


class Gateway(ABC):
    @abstractmethod
    def create_entity(self, entity):
        pass

    @abstractmethod
    def read_entity(self, query_object) -> Entity:
        pass

    @abstractmethod
    def read_all_entities(self, query_object) -> Entity:
        pass

    @abstractmethod
    def update_entity(self, entity):
        pass


    @abstractmethod
    def delete_entity(self, entity):
        pass
