import unittest

from yearsinpixels_data.EntityMap.DatatypeBoolean import DatatypeBoolean
from yearsinpixels_data.EntityMap.MySQLDatatypeBoolean import MySQLDatatypeBoolean
from yearsinpixels_data.EntityMap.MySQLDatatypeInteger import MySQLDatatypeInteger


class MySQLDatatypeIntegerTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(MySQLDatatypeInteger)

    def test_is_datatype(self):
        self.assertTrue(issubclass(MySQLDatatypeBoolean, DatatypeBoolean))

    def test_convert_to_database(self):
        result_true = MySQLDatatypeBoolean().convert_to_database(True)
        result_false = MySQLDatatypeBoolean().convert_to_database(False)
        self.assertTrue(isinstance(result_true, str))
        self.assertEqual('1', result_true)
        self.assertEqual('0', result_false)

        with self.assertRaises(Exception) as context:
            MySQLDatatypeBoolean().convert_to_database("asdf")

    def test_convert_from_database(self):
        pass
