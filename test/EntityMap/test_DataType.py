import unittest

from yearsinpixels_data.EntityMap.Datatype import Datatype


class DatatypeTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(Datatype)

    def test_content(self):
        self.assertIsNotNone(Datatype.INTEGER)
        self.assertIsNotNone(Datatype.STRING)
        self.assertIsNotNone(Datatype.BOOLEAN)
        self.assertIsNotNone(Datatype.DATETIME)

