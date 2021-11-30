import unittest
from abc import ABC

from yearsinpixels_data.EntityMap.Datatype import Datatype


class DatatypeTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(Datatype)

    def test_is_abstract(self):
        self.assertTrue(issubclass(Datatype, ABC))

    def test_has_convert_methods(self):
        self.assertIsNotNone(Datatype.convert_to_database)
        self.assertIsNotNone(Datatype.convert_from_database)