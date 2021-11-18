import unittest
from abc import ABC, abstractmethod

from yearsinpixels_data.Gateway.Gateway import Gateway


class GatewayTest(unittest.TestCase):

    def test_is_there(self):
        self.assertTrue(Gateway)

    def test_is_abstract(self):
        self.assertTrue(issubclass(Gateway, ABC))

    def test_methods(self):
        self.assertIsNotNone(Gateway.create_entity)
        self.assertIsNotNone(Gateway.read_entity)
        self.assertIsNotNone(Gateway.update_entity)
        self.assertIsNotNone(Gateway.delete_entity)
