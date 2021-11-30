import unittest

from yearsinpixels_data.EntityMap.Datapair import Datapair
from yearsinpixels_data.EntityMap.DatatypeInteger import DatatypeInteger


class DataPairTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(Datapair)

    def test_construction(self):
        datatype = DatatypeInteger
        field_name = "some_field_name"
        datapair = Datapair(datatype, field_name)
        self.assertEqual(datapair.datatype, datatype)
        self.assertEqual(datapair.field_name, field_name)


