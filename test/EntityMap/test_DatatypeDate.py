from datetime import date
import unittest

from yearsinpixels_data.EntityMap.Datatype import Datatype
from yearsinpixels_data.EntityMap.DatatypeDate import DatatypeDate


class DatatypeDateTest(unittest.TestCase):
    def test_is_ther(self):
        self.assertIsNotNone(DatatypeDate)

    def test_inheritance(self):
        self.assertTrue(issubclass(DatatypeDate, Datatype))

    def test_convert_to_database(self):
        datatype = DatatypeDate()
        today = date.today()
        db_string = datatype.convert_to_database(today)
        self.assertEqual(f"{today.year}-{today.month}-{today.day}", db_string)

    def test_convert_from_database(self):
        datatype = DatatypeDate()
        today = date.today()
        self.assertEqual(today, datatype.convert_from_database(today))