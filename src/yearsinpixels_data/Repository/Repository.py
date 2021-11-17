from abc import abstractmethod, ABC


class Repository(ABC):

    @abstractmethod
    def initialize(self, data_strategy):
        pass

    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def read(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass

