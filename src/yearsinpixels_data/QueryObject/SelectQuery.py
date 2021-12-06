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
        gen_query = "SELECT "

        entity_map = ConcreteEntityMapFactory.construct(self.entity)

        for field_name in dir(entity_map):
            if field_name.startswith("_") or field_name.startswith("get"): continue
            gen_query += f"{field_name}, "
        gen_query = gen_query[:len(gen_query) - 2]

        gen_query += f" FROM {entity_map.get_common_name()} WHERE"

        iterator = 0
        for criteria in self.criteria:
            gen_query += criteria.generate_sql()
            if iterator + 1 != len(self.criteria):
                gen_query += " AND "
            iterator += 1
        return gen_query
