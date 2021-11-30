from yearsinpixels_data.EntityMap.ConcreteEntityMapFactory import ConcreteEntityMapFactory
from yearsinpixels_data.QueryObject.QueryObject import QueryObject


class InsertQuery(QueryObject):

    def __init__(self, entity):
        self.entity = entity
        self.type = type(entity)


    def generate_sql(self):
        sql_code = "INSERT INTO "
        entity_map = ConcreteEntityMapFactory.construct(self.type)
        sql_map = self.merge_entity_with_datamap(self.entity, entity_map)

        print(2)

        sql_code += str(entity_map.get_common_name())
        sql_code += " ("
        for field in dir(self.entity):
            if field.startswith("_"): continue
            sql_code += f"{field}, "
        # Delete the last two characters ', ' from the sql code.
        sql_code = sql_code[:len(sql_code) - 2]
        sql_code += ") "
        sql_code += "VALUES"
        sql_code += " ("
        for field in dir(self.entity):
            if field.startswith("_"): continue
            sql_code += f"'{getattr(self.entity, field)}', "
        # Delete the last two characters ', ' from the sql code.
        sql_code = sql_code[:len(sql_code) - 2]
        sql_code += ");"

        return sql_code

    def merge_entity_with_datamap(self, entity, map):
        # return dict of type <datapair(field_name, datatype), value>
        entity_as_map = dict()
        output = dict()
        # Add the bare entity to the map
        for field in dir(entity):
            if field.startswith("_"): continue
            entity_as_map[field] = getattr(entity, field)

        # set the proper field name from the entity map
        for key, value in entity_as_map.items():
            new_key = getattr(map, key)
            output[new_key] = value

        del entity_as_map
        return output
