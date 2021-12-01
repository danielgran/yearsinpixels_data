from yearsinpixels_business.Entity.Entity import Entity

from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria
from yearsinpixels_data.QueryObject.QueryObject import QueryObject


class SelectQuery(QueryObject):

    def __init__(self, entity):
        if not issubclass(entity, Entity):
            raise Exception("Can only be instanciated with Business objects.")

        self.entity = entity
        self.type = type(entity)
        self.criteria = list()

    def generate_sql(self):
        gen_query = "SELECT * FROM user WHERE "
        iterator = 0
        for criteria in self.criteria:
            gen_query += criteria.generate_sql()
            if iterator + 1 != len(self.criteria):
                gen_query += " AND "
            iterator += 1
        gen_query += ";"
        return gen_query