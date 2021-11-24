import unittest
from abc import ABC

from yearsinpixels_data.EntityMap.EntityMap import EntityMap
from yearsinpixels_data.EntityMap.UserMap import UserMap


class EntityMapTest(unittest.TestCase):
    def test_is_there_and_is_abstract(self):
        self.assertIsNotNone(EntityMap)
        self.assertTrue(issubclass(EntityMap, ABC))

    def test_meta(self):
        self.assertIsNotNone(EntityMap.get_common_name)


class TestMaps(unittest.TestCase):
    def test_usermap(self):
        usermap = UserMap()
        self.assertTrue(issubclass(UserMap, EntityMap) and len(usermap.get_common_name()) > 0)