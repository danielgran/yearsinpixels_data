import unittest

from yearsinpixels_data.Gateway.Gateway import Gateway
from yearsinpixels_data.Gateway.MySQLGateway import MySQLGateway


class MySQLGatewayTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(MySQLGateway)

    def test_is_gateway(self):
        self.assertTrue(issubclass(MySQLGateway, Gateway))
