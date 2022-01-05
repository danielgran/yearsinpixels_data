import unittest

import test
from yearsinpixels_data.Database.MySQLConnection import MySQLConnection

@unittest.skipIf(test.disable_mysql_testcase,
                 "MySQL support will not work on this system. Use the 'yearsinpixels_data.Gateway.TestGateway' package.")
class MySQLConnectionTest(unittest.TestCase):
    def setUp(self):
        self.mysqlconnection = MySQLConnection()
        self.mysqlconnection.username = "root"
        self.mysqlconnection.password = "somepass"
        self.mysqlconnection.database = "yearsinpixels"

    def test_is_there(self):
        self.assertIsNotNone(MySQLConnection)

    def test_metadata(self):
        self.assertIsNotNone(self.mysqlconnection.host)
        self.assertIsNotNone(self.mysqlconnection.port)
        self.assertIsNotNone(self.mysqlconnection.database)
        self.assertIsNotNone(self.mysqlconnection.username)
        self.assertIsNotNone(self.mysqlconnection.password)
        self.assertEqual(self.mysqlconnection.connected, False)

    def test_connectivity(self):
        self.mysqlconnection.connect()
        self.assertIsNotNone(self.mysqlconnection.connection)
        self.mysqlconnection.disconnect()

    def test_is_connected(self):
        self.mysqlconnection.connect()
        self.assertTrue(self.mysqlconnection.is_connected)

    def test_is_connected_after_external_disconnect(self):
        self.mysqlconnection.connect()
        self.mysqlconnection.connection.cmd_quit()
        self.assertTrue(self.mysqlconnection.is_connected == False)



