import unittest

from yearsinpixels_data.Gateway.Gateway import Gateway
from yearsinpixels_data.Gateway.MySQLGateway import MySQLGateway



skip = None
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

    def test_connect(self):
        self.gateway.connect()

    def test_disconnect(self):
        self.gateway.connect()
        self.gateway.disconnect()
