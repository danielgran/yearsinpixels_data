import unittest

from yearsinpixels_data.EntityMap.Datatype import Datatype
from yearsinpixels_data.EntityMap.MySQLDatatypeString import MySQLDatatypeString


class MySQLDatatypeStringTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(MySQLDatatypeString)

    def test_is_datatype(self):
        self.assertTrue(issubclass(MySQLDatatypeString, Datatype))

    def test_convert_to_database(self):
        value = "This shuld be converted to the database"
        result = MySQLDatatypeString().convert_to_database(value)
        self.assertTrue(isinstance(result, str))

        self.assertEqual(str(value), result)

        with self.assertRaises(Exception) as context:
            MySQLDatatypeString().convert_to_database(123)

    def test_convert_from_database_normal_string(self):
        string = "This is a string for testing purposes"
        self.assertEqual(string, MySQLDatatypeString().convert_from_database(string))

    def test_convert_from_database_bytes(self):
        bytes = b"This is a string for testing purposes"
        self.assertEqual(bytes.decode('utf-8'), MySQLDatatypeString().convert_from_database(bytes))