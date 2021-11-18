import unittest
from abc import ABC

from yearsinpixels_data.Database.Database import DatabaseStrategy


class DatabaseTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(DatabaseStrategy)

    def test_meta(self):
        self.assertTrue(issubclass(DatabaseStrategy, ABC))
        self.assertIsNotNone(DatabaseStrategy.connect)
        self.assertIsNotNone(DatabaseStrategy.disconnect)
        self.assertIsNotNone(DatabaseStrategy.query)
