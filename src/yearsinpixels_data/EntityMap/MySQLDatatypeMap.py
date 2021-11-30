from yearsinpixels_data.EntityMap.DatatypeBoolean import DatatypeBoolean
from yearsinpixels_data.EntityMap.DatatypeDatetime import DatatypeDatetime
from yearsinpixels_data.EntityMap.DatatypeInteger import DatatypeInteger
from yearsinpixels_data.EntityMap.DatatypeString import DatatypeString
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

    def get_mysql_type(self, datatype):
        if issubclass(datatype, DatatypeInteger):
            return self.integer

        if issubclass(datatype, DatatypeBoolean):
            return self.boolean

        if issubclass(datatype, DatatypeString):
            return self.string

        if issubclass(datatype, DatatypeDatetime):
            return self.datetime


