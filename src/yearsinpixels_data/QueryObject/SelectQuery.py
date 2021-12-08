from yearsinpixels_business.Entity.Entity import Entity

from yearsinpixels_data.EntityMap.ConcreteEntityMapFactory import ConcreteEntityMapFactory
from yearsinpixels_data.QueryObject.QueryObject import QueryObject


class SelectQuery(QueryObject):

    def __init__(self, entity):
        if not issubclass(entity, Entity):
            raise Exception("Can only be instanciated with Business objects.")

        self.entity = entity
        self.criteria = list()

    def generate_sql(self):
        generated_query = "SELECT "

        entity_map = ConcreteEntityMapFactory.construct(self.entity)

        for field_name in dir(entity_map):
            if field_name.startswith("_") or field_name.startswith("get"): continue
            generated_query += f"{field_name}, "
        generated_query = generated_query[:len(generated_query) - 2]

        generated_query += f" FROM {entity_map.get_common_name()}"

        if len(self.criteria) == 0:
            return generated_query

        generated_query += " WHERE "
        iterator = 0
        for criteria in self.criteria:
            generated_query += criteria.generate_sql()
            if iterator + 1 != len(self.criteria):
                generated_query += " AND "
            iterator += 1
        return generated_query
