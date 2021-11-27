import unittest

from yearsinpixels_data.EntityMap.DataPair import DataPair


class DataPairTest(unittest.TestCase):
    def test_is_there(self):
        self.assertTrue(self.assertIsNotNone(DataPair))

    def test_construction(self):
        datapair = DataPair()


