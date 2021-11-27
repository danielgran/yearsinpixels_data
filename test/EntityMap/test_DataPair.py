import unittest

from yearsinpixels_data.EntityMap.DataPair import DataPair
from yearsinpixels_data.EntityMap.Datatype import Datatype


class DataPairTest(unittest.TestCase):
    def test_is_there(self):
        self.assertTrue(self.assertIsNotNone(DataPair))

    def test_construction(self):
        datatype = Datatype.INTEGER
        field_name = "some_field_name"
        datapair = DataPair(datatype, field_name)
        self.assertEqual(datapair.datatype, datatype)
        self.assertEqual(datapair.field_name, field_name)


