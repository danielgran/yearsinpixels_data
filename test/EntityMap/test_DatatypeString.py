import unittest
from abc import ABC

from yearsinpixels_data.EntityMap.Datatype import Datatype
from yearsinpixels_data.EntityMap.DatatypeDatetime import DatatypeString


class DatatypeStringTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(DatatypeString)

    def test_inheritance(self):
        self.assertTrue(issubclass(DatatypeString, ABC))
        self.assertTrue(issubclass(DatatypeString, Datatype))
