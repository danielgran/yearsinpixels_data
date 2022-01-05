from mysql.connector import connect
from yearsinpixels_business.Entity.Entity import Entity

from yearsinpixels_data.EntityMap.ConcreteEntityMapFactory import ConcreteEntityMapFactory
from yearsinpixels_data.EntityMap.MySQLDatatypeMap import MySQLDatatypeMap
from yearsinpixels_data.Gateway.Gateway import Gateway
from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria
from yearsinpixels_data.QueryObject.InsertQuery import InsertQuery
from yearsinpixels_data.QueryObject.UpdateQuery import UpdateQuery


class MySQLGateway(Gateway):
    def __init__(self, mysqlconnection):
        self.connection = mysqlconnection

    def connect(self):
        try:
            self.connection = connect(user=self.username, password=self.password, host=self.host, port=self.port,
                                      database=self.database)
            cursor = self.connection.cursor()
            cursor.execute("SET NAMES utf8mb4")
            cursor.execute("SET CHARACTER SET utf8mb4")
            cursor.execute("SET character_set_connection=utf8mb4")
            self.connection.commit()
            cursor.close()
            self.connection.autocommit = True
        except:
            raise

    def disconnect(self):
        try:
            self.connection.disconnect()
        except:
            raise

    def create_entity(self, entity):
        query = InsertQuery(entity).generate_sql()
        self.connection.query(query, vars(entity))

    def read_entity(self, select_query) -> Entity:
        query = select_query.generate_sql()
        cursor = self.connection.cursor(dictionary=True)
        criteria_as_dict = {str(key.field): key.value for key in select_query.criteria}
        cursor.execute(query, criteria_as_dict)

        entity_from_database = None
        for entity in cursor:
            entity_from_database = self.read_single_entity_from_cursor_iteratable(entity, select_query.entity)
            break  # Only the first entity

        cursor.close()
        return entity_from_database

    def read_all_entities(self, select_query) -> Entity:
        query = select_query.generate_sql()
        cursor = self.connection.cursor(dictionary=True)
        criteria_as_dict = {str(key.field): key.value for key in select_query.criteria}
        cursor.execute(query, criteria_as_dict)

        entities_from_database = list()
        for entity in cursor:
            entities_from_database.append(self.read_single_entity_from_cursor_iteratable(entity, select_query.entity))
        cursor.close()

        return entities_from_database

    def read_single_entity_from_cursor_iteratable(self, cursor_iteratabe, output_type):
        entity_map = ConcreteEntityMapFactory().construct(output_type)
        constructed_entity = output_type()
        for field in cursor_iteratabe.keys():
            field_name_from_database = field
            value_from_database = cursor_iteratabe[field_name_from_database]
            datapair = getattr(entity_map, field_name_from_database)
            sql_datatype = MySQLDatatypeMap().get_mysql_type(datapair.datatype)()
            converted_value = sql_datatype.convert_from_database(value_from_database)
            setattr(constructed_entity, datapair.field_name, converted_value)
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
        criteria_as_dict = {str(key.field): key.value for key in update_query.criteria}
        cursor.execute(query, criteria_as_dict)
        self.connection.commit()
        cursor.close()

    def delete_entity(self, entity):
        pass
