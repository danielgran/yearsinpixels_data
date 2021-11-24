import unittest

from yearsinpixels_data.EntityMap.EntityMap import EntityMap
from yearsinpixels_data.EntityMap.UserMap import UserMap


class UserMapTest(unittest.TestCase):
    def test_usermap(self):
        usermap = UserMap()
        self.assertTrue(issubclass(UserMap, EntityMap) and len(usermap.get_common_name()) > 0)

    def test_attrs(self):
        usermap = UserMap()
        for var in dir(usermap):
            if var.startswith("_") or var.startswith("get"):
                continue

            return_value_from_property = getattr(usermap, var)
            self.assertTrue(isinstance(return_value_from_property, str) and len(return_value_from_property) > 0)
