from abc import ABC, abstractmethod


class EntityMap(ABC):

    @abstractmethod
    def get_common_name(self):
        pass

    @abstractmethod
    def get_primary_identifier_field(self):
        pass
