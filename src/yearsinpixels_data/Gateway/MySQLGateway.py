from mysql.connector import connect
from yearsinpixels_business.Entity.Entity import Entity

from yearsinpixels_data.EntityMap.ConcreteEntityMapFactory import ConcreteEntityMapFactory
from yearsinpixels_data.EntityMap.MySQLDatatypeMap import MySQLDatatypeMap
from yearsinpixels_data.Gateway.Gateway import Gateway
from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria
from yearsinpixels_data.QueryObject.InsertQuery import InsertQuery
from yearsinpixels_data.QueryObject.UpdateQuery import UpdateQuery


class MySQLGateway(Gateway):
    def __init__(self, username='', password='', host='', port=3306, database=None):
        assert database is not None
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database

        self.connection = None

    def connect(self):
        try:
            self.connection = connect(user=self.username, password=self.password, host=self.host, port=self.port,
                                      database=self.database)
        except:
            raise

    def disconnect(self):
        try:
            self.connection.disconnect()
        except:
            raise

    def create_entity(self, entity):
        query = InsertQuery(entity).generate_sql()
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def read_entity(self, query_object) -> Entity:

        query = query_object.generate_sql()
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)

        entity_map = ConcreteEntityMapFactory().construct(query_object.entity)
        constructed_entity = query_object.entity()

        for entity in cursor:
            for field in entity.keys():
                field_name_from_database = field
                value_from_database = entity[field_name_from_database]
                datapair = getattr(entity_map, field_name_from_database)
                sql_datatype = MySQLDatatypeMap().get_mysql_type(datapair.datatype)()
                converted_value = sql_datatype.convert_from_database(value_from_database)
                setattr(constructed_entity, datapair.field_name, converted_value)
            break  # Only the first entity
        cursor.close()

        return constructed_entity

    def update_entity(self, entity):
        business_object_class = type(entity)
        entity_map = ConcreteEntityMapFactory.construct(business_object_class)
        primary_identifier_name = entity_map.get_primary_identifier_field().field_name

        update_query = UpdateQuery(business_object_class)
        update_query.add_criteria(Criteria.matches(primary_identifier_name, getattr(entity, primary_identifier_name)))
        update_query.set_update_object(entity)

        query = update_query.generate_sql()

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def delete_entity(self, entity):
        pass
