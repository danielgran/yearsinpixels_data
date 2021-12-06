import unittest

from yearsinpixels_data.EntityMap import MySQLDatatypeDate
from yearsinpixels_data.EntityMap.DatatypeBoolean import DatatypeBoolean
from yearsinpixels_data.EntityMap.DatatypeDate import DatatypeDate
from yearsinpixels_data.EntityMap.DatatypeDatetime import DatatypeDatetime
from yearsinpixels_data.EntityMap.DatatypeInteger import DatatypeInteger
from yearsinpixels_data.EntityMap.DatatypeString import DatatypeString
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
        self.assertEqual(MySQLDatatypeDate, dtmap.date)

    def test_get_func(self):
        dtmap = MySQLDatatypeMap()
        self.assertEqual(MySQLDatatypeInteger, dtmap.get_mysql_type(DatatypeInteger))
        self.assertEqual(MySQLDatatypeBoolean, dtmap.get_mysql_type(DatatypeBoolean))
        self.assertEqual(MySQLDatatypeString, dtmap.get_mysql_type(DatatypeString))
        self.assertEqual(MySQLDatatypeDatetime, dtmap.get_mysql_type(DatatypeDatetime))
        self.assertEqual(MySQLDatatypeDate, dtmap.get_mysql_type(DatatypeDate))
