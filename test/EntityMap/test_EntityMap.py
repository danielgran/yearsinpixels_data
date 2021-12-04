import unittest
from abc import ABC

from yearsinpixels_data.EntityMap.EntityMap import EntityMap


class EntityMapTest(unittest.TestCase):
    def test_is_there_and_is_abstract(self):
        self.assertIsNotNone(EntityMap)
        self.assertTrue(issubclass(EntityMap, ABC))

    def test_meta(self):
        self.assertIsNotNone(EntityMap.get_common_name)
        self.assertIsNotNone(EntityMap.get_primary_identifier_field)
