import unittest

from yearsinpixels_data.EntityMap.EntityMap import EntityMap
from yearsinpixels_data.EntityMap.MoodMap import MoodMap


class MoodMapTest(unittest.TestCase):
    def test_usermap(self):
        usermap = MoodMap()
        self.assertTrue(issubclass(MoodMap, EntityMap) and len(usermap.get_common_name()) > 0)

    def test_attrs(self):
        daymap = MoodMap()
        for var in dir(daymap):
            if var.startswith("_") or var.startswith("get"):
                continue

            data_pair_from_property = getattr(daymap, var)
            self.assertTrue(var in dir(daymap))
            self.assertTrue(
                isinstance(data_pair_from_property.field_name, str) and len(data_pair_from_property.field_name) > 0)

    def test_get_primary_identifier(self):
        usermap = MoodMap()
        self.assertIsNone(usermap.get_primary_identifier_field())
