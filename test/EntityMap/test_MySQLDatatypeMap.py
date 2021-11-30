import unittest

from yearsinpixels_data.EntityMap.MySQLDatatypeBoolean import MySQLDatatypeBoolean
from yearsinpixels_data.EntityMap.MySQLDatatypeDatetime import MySQLDatatypeDatetime
from yearsinpixels_data.EntityMap.MySQLDatatypeInteger import MySQLDatatypeInteger
from yearsinpixels_data.EntityMap.MySQLDatatypeMap import MySQLDatatypeMap
from yearsinpixels_data.EntityMap.MySQLDatatypeString import MySQLDatatypeString



class MySQLDatatypeMapTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(MySQLDatatypeMap)

    def test_datatypes(self):
        dtmap = MySQLDatatypeMap()
        self.assertEqual(MySQLDatatypeInteger, dtmap.integer)
        self.assertEqual(MySQLDatatypeBoolean, dtmap.boolean)
        self.assertEqual(MySQLDatatypeString, dtmap.string)
        self.assertEqual(MySQLDatatypeDatetime, dtmap.datetime)
