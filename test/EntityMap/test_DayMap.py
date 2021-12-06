import unittest

from yearsinpixels_data.EntityMap.DayMap import DayMap
from yearsinpixels_data.EntityMap.EntityMap import EntityMap


class UserMapTest(unittest.TestCase):
    def test_usermap(self):
        usermap = DayMap()
        self.assertTrue(issubclass(DayMap, EntityMap) and len(usermap.get_common_name()) > 0)

    def test_attrs(self):
        daymap = DayMap()
        for var in dir(daymap):
            if var.startswith("_") or var.startswith("get"):
                continue

            data_pair_from_property = getattr(daymap, var)
            self.assertTrue(var in dir(daymap))
            self.assertTrue(
                isinstance(data_pair_from_property.field_name, str) and len(data_pair_from_property.field_name) > 0)

    def test_get_primary_identifier(self):
        usermap = DayMap()
        self.assertIsNone(usermap.get_primary_identifier_field())
