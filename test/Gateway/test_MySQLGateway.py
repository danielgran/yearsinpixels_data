import unittest
import uuid
from datetime import datetime
from hashlib import md5

from yearsinpixels_business.Entity.User import User
from yearsinpixels_data.Gateway.Gateway import Gateway
from yearsinpixels_data.Gateway.MySQLGateway import MySQLGateway
from yearsinpixels_data.QueryObject.Criteria.MatchCriteria import MatchCriteria
from yearsinpixels_data.QueryObject.SelectQuery import SelectQuery



try:
    import mysql.connector

    connection = mysql.connector.connect(user='root', database='yearsinpixels', password='somepass')
    connection.close()
    skip = False
except:
    skip = True


@unittest.skipIf(skip,
                 "MySQL support will not work on this system. Use the 'yearsinpixels_data.Gateway.TestGateway' package.")
class MySQLGatewayTest(unittest.TestCase):
    def setUp(self):
        username = "root"
        password = "somepass"
        host = "localhost"
        port = 3306
        database = "yearsinpixels"
        self.gateway = MySQLGateway(username=username, password=password, host=host, port=port, database=database)
        self.gateway.connect()

    def test_is_there(self):
        self.assertIsNotNone(MySQLGateway)

    def test_is_gateway(self):
        self.assertTrue(issubclass(MySQLGateway, Gateway))

    def test_connectivity(self):
        self.gateway.disconnect()

    def test_create_entity(self):
        user = User()
        user.email = str(uuid.uuid4())

        self.gateway.create_entity(user)

    def test_read_entity(self):
        user = User()

        # replace microseconds from cache user
        for field in dir(user):
            if isinstance(getattr(user, field), datetime):
                setattr(user, field, getattr(user, field).replace(microsecond=0))

        user.email = str(uuid.uuid4())
        self.gateway.create_entity(user)

        select_query = SelectQuery(User)
        select_query.add_criteria(MatchCriteria("guid", user.guid))
        user_from_database = self.gateway.read_entity(select_query)

        hash_user = self.hash_entity(user)
        hash_user_from_database = self.hash_entity(user_from_database)

        self.assertTrue(hash_user.hexdigest() == hash_user_from_database.hexdigest())

    def hash_entity(self, entity):
        string = ""
        for field in dir(entity):
            if field.startswith("_"): continue
            string += field + str(getattr(entity, field))
        #return string
        return md5(bytes(string, encoding='utf8'))
