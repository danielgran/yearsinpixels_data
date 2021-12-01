import unittest

from yearsinpixels_data.EntityMap.DatatypeBoolean import DatatypeBoolean
from yearsinpixels_data.EntityMap.MySQLDatatypeBoolean import MySQLDatatypeBoolean


class MySQLDatatypeBooleanTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(MySQLDatatypeBoolean)

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
        true_value_from_database = 1
        false_value_from_database = 0
        self.assertEqual(True, MySQLDatatypeBoolean().convert_from_database(true_value_from_database))
        self.assertEqual(False, MySQLDatatypeBoolean().convert_from_database(false_value_from_database))


    def test_convert_from_database_detect_wrong_data(self):

        self.assertRaises(Exception, MySQLDatatypeBoolean().convert_to_database, 2)
        self.assertRaises(Exception, MySQLDatatypeBoolean().convert_to_database, 11)
        self.assertRaises(Exception, MySQLDatatypeBoolean().convert_to_database, "asdf")
