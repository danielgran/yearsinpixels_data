from abc import ABC
import unittest

from yearsinpixels_data.EntityMap.Datatype import Datatype
from yearsinpixels_data.EntityMap.DatatypeDate import DatatypeDate


class DatatypeDateTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(DatatypeDate)

    def test_inheritance(self):
        self.assertTrue(issubclass(DatatypeDate, ABC))
        self.assertTrue(issubclass(DatatypeDate, Datatype))