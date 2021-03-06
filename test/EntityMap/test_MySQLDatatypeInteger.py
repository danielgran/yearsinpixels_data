import unittest

from yearsinpixels_data.EntityMap.DatatypeInteger import DatatypeInteger
from yearsinpixels_data.EntityMap.MySQLDatatypeInteger import MySQLDatatypeInteger


class MySQLDatatypeIntegerTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(MySQLDatatypeInteger)

    def test_is_datatype(self):
        self.assertTrue(issubclass(MySQLDatatypeInteger, DatatypeInteger))

    def test_convert_to_database(self):
        integer = 99999999999999999
        result = MySQLDatatypeInteger().convert_to_database(integer)
        self.assertTrue(isinstance(result, str))
        self.assertEqual(str(integer), result)

        with self.assertRaises(Exception) as context:
            MySQLDatatypeInteger().convert_to_database("asdf")


    def test_convert_from_database(self):
        integer = 123
        self.assertEqual(integer, MySQLDatatypeInteger().convert_from_database(123))