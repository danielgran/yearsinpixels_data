import inspect
import unittest
from abc import ABC

from yearsinpixels_data.Security.DataEscaper.StringEscaper import StringEscaper


class StringEscaperTest(unittest.TestCase):
    def test_is_abstract(self):
        self.assertTrue(issubclass(StringEscaper, ABC))

    def test_escape_string(self):
        self.assertIsNotNone(StringEscaper.escape)

    def test_signature(self):
        signature = inspect.signature((StringEscaper.escape))
        self.assertIsNotNone(signature.parameters.get("string"))