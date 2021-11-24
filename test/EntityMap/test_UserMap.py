import unittest

from yearsinpixels_data.EntityMap.EntityMap import EntityMap
from yearsinpixels_data.EntityMap.UserMap import UserMap


class UserMapTest(unittest.TestCase):
    def test_usermap(self):
        usermap = UserMap()
        self.assertTrue(issubclass(UserMap, EntityMap) and len(usermap.get_common_name()) > 0)