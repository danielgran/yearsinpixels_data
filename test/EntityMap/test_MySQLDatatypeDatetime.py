import time
import unittest

from yearsinpixels_data.EntityMap.DatatypeDatetime import DatatypeDatetime
from yearsinpixels_data.EntityMap.MySQLDatatypeDatetime import MySQLDatatypeDatetime


class MySQLDatatypeDatetimeTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(MySQLDatatypeDatetime)

    def test_is_datatype(self):
        self.assertTrue(issubclass(MySQLDatatypeDatetime, DatatypeDatetime))

    def test_convert_to_database(self):
        datetime = time.time()
        result = MySQLDatatypeDatetime().convert_to_database(datetime)
        self.assertTrue(isinstance(result, str))
        self.assertTrue("." not in result, "Conversion to int failed")

        with self.assertRaises(Exception) as context:
            MySQLDatatypeDatetime().convert_to_database("This should fail.")

    def test_convert_from_database(self):
        pass