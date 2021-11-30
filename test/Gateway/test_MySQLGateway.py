import unittest

from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.EntityMap.UserMap import UserMap
from yearsinpixels_data.Gateway.Gateway import Gateway
from yearsinpixels_data.Gateway.MySQLGateway import MySQLGateway
from yearsinpixels_data.QueryObject.Criteria.MatchCriteria import MatchCriteria

try:
    import mysql.connector
    connection = mysql.connector.connect(user='root', database='yearsinpixels', password='somepass')
    connection.close()
    skip = False
except:
    skip = True

@unittest.skipIf(skip, "MySQL support will not work on this system. Use the 'yearsinpixels_data.Gateway.TestGateway' package.")
class MySQLGatewayTest(unittest.TestCase):
    def setUp(self):
        username = "root"
        password = "somepass"
        host = "localhost"
        port = 3306
        database = "yearsinpixels"
        self.gateway = MySQLGateway(username=username, password=password, host=host, port=port, database=database)

    def test_is_there(self):
        self.assertIsNotNone(MySQLGateway)

    def test_is_gateway(self):
        self.assertTrue(issubclass(MySQLGateway, Gateway))

    def test_connectivity(self):
        self.gateway.connect()
        self.gateway.disconnect()

    def test_create_entity(self):
        self.gateway.connect()

        user = User()

        self.gateway.create_entity(user)

        field = UserMap().guid.field_name
        criteria = MatchCriteria(field, user.guid)
        self.assertIsNotNone(self.gateway.read_entity(user, criteria))

























