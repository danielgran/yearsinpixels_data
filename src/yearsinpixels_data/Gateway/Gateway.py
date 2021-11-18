from abc import ABC, abstractmethod


class Gateway(ABC):
    @abstractmethod
    def create_entity(self):
        pass

    @abstractmethod
    def read_entity(self):
        pass

    @abstractmethod
    def update_entity(self):
        pass

    @abstractmethod
    def delete_entity(self):
        pass
