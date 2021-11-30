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
        try:
            self.connection = connect(user=self.username, password=self.password, host=self.host, port=self.port, database=self.database)
        except:
            raise

    def disconnect(self):
        try:
            self.connection.disconnect()
        except:
            raise

    def create_entity(self, entity):
        pass

    def read_entity(self, entity, criteria) -> Entity:
        pass

    def update_entity(self, entity):
        pass

    def delete_entity(self, entity):
        pass



