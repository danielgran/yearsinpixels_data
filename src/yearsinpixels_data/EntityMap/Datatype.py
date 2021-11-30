from abc import ABC, abstractmethod


class Datatype(ABC):

    @abstractmethod
    def convert_to_database(self, element):
        pass

    @abstractmethod
    def convert_from_database(self, element):
        pass
