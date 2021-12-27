import unittest

from yearsinpixels_data.Security.DataEscaper.StringEscaper import StringEscaper
from yearsinpixels_data.Security.DataEscaper.MySQLStringEscaper import MySQLStringEscaper


class MySQLStringEscaperTest(unittest.TestCase):
    def setUp(self):
        self.string_escaper = MySQLStringEscaper()

    def test_is_data_escaper(self):
        self.assertTrue(issubclass(MySQLStringEscaper, StringEscaper))