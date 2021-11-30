import unittest
from abc import ABC

from yearsinpixels_data.EntityMap.Datatype import Datatype
from yearsinpixels_data.EntityMap.DatatypeInteger import DatatypeInteger


class DatatypeIntegerTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(DatatypeInteger)

    def test_inheritance(self):
        self.assertTrue(issubclass(DatatypeInteger, ABC))
        self.assertTrue(issubclass(DatatypeInteger, Datatype))
