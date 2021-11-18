from abc import ABC, abstractmethod


class QueryObject(ABC):
    def __init__(self):
        self.criteria = list()

    @abstractmethod
    def generate_sql(self):
        pass

    def addCriteria(self, criteria):
        self.criteria.append(criteria)

