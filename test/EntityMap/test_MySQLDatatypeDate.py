import unittest
from datetime import date

from yearsinpixels_data.EntityMap.MySQLDatatypeDate import MySQLDatatypeDate


class MySQLDatatypeDateTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(MySQLDatatypeDate)

    def test_is_datatype(self):
        self.assertTrue(issubclass(MySQLDatatypeDate, MySQLDatatypeDate))

    def test_convert_to_database(self):
        datatype = MySQLDatatypeDate()
        today = date.today()
        db_string = datatype.convert_to_database(today)
        self.assertEqual(f"{today.year}-{today.month}-{today.day}", db_string)

    def test_convert_from_database(self):
        datatype = MySQLDatatypeDate()
        today = date.today()
        self.assertEqual(today, datatype.convert_from_database(today))

    def test_convert_from_database_detect_wrong_data(self):
        self.assertRaises(Exception, MySQLDatatypeDate().convert_to_database, 2)
        self.assertRaises(Exception, MySQLDatatypeDate().convert_to_database, 11)
        self.assertRaises(Exception, MySQLDatatypeDate().convert_to_database, "asdf")