import unittest
from abc import ABC

from yearsinpixels_data.EntityMap.Datatype import Datatype
from yearsinpixels_data.EntityMap.DatatypeBoolean import DatatypeBoolean


class DatatypeBooleanTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(DatatypeBoolean)

    def test_inheritance(self):
        self.assertTrue(issubclass(DatatypeBoolean, ABC))
        self.assertTrue(issubclass(DatatypeBoolean, Datatype))
