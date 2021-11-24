from mysql.connector import connect
from yearsinpixels_business.Entity.Entity import Entity

from yearsinpixels_data.Gateway.Gateway import Gateway


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
        success = False
        try:
            self.connection = connect(user=self.username, password=self.password, host=self.host, port=self.port, database=self.database)
            success = True
        except:
            success = False
        return success

    def disconnect(self):
        success = False
        try:
            self.connection.disconnect()
            success = True
        except:
            success = False
        return success

    def create_entity(self, entity):
        pass

    def read_entity(self, entity, criteria=None) -> Entity:
        pass

    def update_entity(self, entity):
        pass

    def delete_entity(self, entity):
        pass



