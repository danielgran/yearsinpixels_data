from yearsinpixels_data.EntityMap.MySQLDatatypeBoolean import MySQLDatatypeBoolean
from yearsinpixels_data.EntityMap.MySQLDatatypeDatetime import MySQLDatatypeDatetime
from yearsinpixels_data.EntityMap.MySQLDatatypeInteger import MySQLDatatypeInteger
from yearsinpixels_data.EntityMap.MySQLDatatypeString import MySQLDatatypeString


class MySQLDatatypeMap:

    @property
    def integer(self):
        return MySQLDatatypeInteger
    @property
    def boolean(self):
        return MySQLDatatypeBoolean
    @property
    def string(self):
        return MySQLDatatypeString
    @property
    def datetime(self):
        return MySQLDatatypeDatetime
