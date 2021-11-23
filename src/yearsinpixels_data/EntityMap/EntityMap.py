from abc import ABC, abstractmethod


class EntityMap(ABC):

    @abstractmethod
    def get_common_name(self):
        pass