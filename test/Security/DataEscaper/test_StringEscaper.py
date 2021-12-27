import unittest
from abc import ABC

from yearsinpixels_data.Security.DataEscaper.StringEscaper import StringEscaper


class StringEscaperTest(unittest.TestCase):
    def setUp(self):
        self.string_escaper = StringEscaper()


    def test_is_abstract(self):
        self.assertTrue(isinstance(self.string_escaper, ABC))

    def test_escape_string(self):
        self.assertIsNotNone(self.string_escaper.escape)