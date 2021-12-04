import unittest

from yearsinpixels_business.Entity.User import User

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

            data_pair_from_property = getattr(usermap, var)
            self.assertTrue(var in dir(User()))
            self.assertTrue(isinstance(data_pair_from_property.field_name, str) and len(data_pair_from_property.field_name) > 0)

    def test_get_primary_identifier(self):
        usermap = UserMap()
        self.assertIsNotNone(usermap.get_primary_identifier_field())