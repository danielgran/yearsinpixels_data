from inspect import isclass

from yearsinpixels_data.EntityMap.ConcreteEntityMapFactory import ConcreteEntityMapFactory
from yearsinpixels_data.EntityMap.MySQLDatatypeMap import MySQLDatatypeMap
from yearsinpixels_data.QueryObject.QueryObject import QueryObject


class UpdateQuery(QueryObject):

    def __init__(self, business_class):
        if not isclass(business_class): raise Exception("Can only be called with a class")

        self.business_class = business_class
        super().__init__()

    def set_update_object(self, update_object):
        if isclass(update_object): raise Exception("Can only be called with an object.")
        if not isinstance(update_object, self.business_class): raise Exception("Must correspond to the proper class.")
        self.update_object = update_object

    def generate_sql(self):
        entity_map = ConcreteEntityMapFactory.construct(self.business_class)
        generated_sql = f"UPDATE `{entity_map.get_common_name()}` SET "

        update_data = list()
        for field_name in dir(entity_map):
            if field_name.startswith("id"):
                continue
            if field_name.startswith("_") or field_name.startswith("get"): continue
            generated_sql += f"{field_name} = '%s', "
            unconverted_field_value = getattr(self.update_object, field_name)
            datatype = getattr(entity_map, field_name).datatype
            datatype_converter = MySQLDatatypeMap().get_mysql_type(datatype)()
            unconverted_field_value = datatype_converter.convert_to_database(unconverted_field_value)
            update_data.append(unconverted_field_value)
        generated_sql = generated_sql[:len(generated_sql) - 2]
        # format string (perpare query)
        generated_sql = generated_sql % tuple(update_data)

        generated_sql += "WHERE "
        iterator = 0
        for criteria in self.criteria:
            generated_sql += criteria.generate_sql()
            if iterator + 1 != len(self.criteria):
                generated_sql += " AND "
            iterator += 1
        generated_sql += ";"
        return generated_sql


