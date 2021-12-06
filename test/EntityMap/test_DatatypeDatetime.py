import unittest
from abc import ABC

from yearsinpixels_data.EntityMap.Datatype import Datatype
from yearsinpixels_data.EntityMap.DatatypeDatetime import DatatypeDatetime


class DatatypeDatetimeTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(DatatypeDatetime)

    def test_inheritance(self):
        self.assertTrue(issubclass(DatatypeDatetime, ABC))
        self.assertTrue(issubclass(DatatypeDatetime, Datatype))
