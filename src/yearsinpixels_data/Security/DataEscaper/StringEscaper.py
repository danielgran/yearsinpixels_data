from abc import ABC, abstractmethod


class StringEscaper(ABC):
    @abstractmethod
    def escape(self, string):
        pass