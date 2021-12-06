from yearsinpixels_data.EntityMap.ConcreteEntityMapFactory import ConcreteEntityMapFactory
from yearsinpixels_data.QueryObject.QueryObject import QueryObject


class JoinQuery(QueryObject):

    def __init__(self, parent_class, child_class):
        super().__init__()
        self.parent_class = parent_class
        self.child_class = child_class



    def generate_sql(self):
        parent_entity_map = ConcreteEntityMapFactory.construct(self.parent_class)
        child_entity_map = ConcreteEntityMapFactory.construct(self.child_class)
        sql = f"SELECT "

        for field_name in dir(child_entity_map):
            if field_name.startswith("_") or field_name.startswith("get"): continue
            sql += f"b.{field_name}, "
        sql = sql[:len(sql) - 2]

        sql += f" from {parent_entity_map.get_common_name()} a " \
              f"JOIN {child_entity_map.get_common_name()} b ON b.id_{parent_entity_map.get_common_name()} = a.id"
        iterator = 0
        if len(self.criteria) > 0:
            sql += " WHERE "
            for criteria in self.criteria:
                sql += "a."
                sql += criteria.generate_sql()
                if iterator + 1 != len(self.criteria):
                    sql += " AND "
                iterator += 1
        return sql
