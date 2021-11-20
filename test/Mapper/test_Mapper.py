import unittest

from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.Gateway.TestGateway import TestGateway
from yearsinpixels_data.Mapper.Mapper import Mapper
from yearsinpixels_data.QueryObject.Criteria.MatchCriteria import MatchCriteria


class MapperTest(unittest.TestCase):
    def setUp(self):
        test_gateway = TestGateway()
        self.mapper = Mapper(test_gateway)

    def test_is_there(self):
        self.assertIsNotNone(Mapper)

    def test_metadata(self):
        self.assertIsNotNone(self.mapper.gateway)
        self.assertIsNotNone(self.mapper.add)
        self.assertIsNotNone(self.mapper.find)
        self.assertIsNotNone(self.mapper.update)
        self.assertIsNotNone(self.mapper.remove)

    def test_add(self):
        user = User()
        user.email = "some@nice.liame"
        self.mapper.add(user)
        # lacking check

    def test_find(self):
        user = User()
        user.name_first = "Programmer Jeff"
        self.mapper.gateway.items.append(user)
        user_from_mapper = self.mapper.find(MatchCriteria('name', user.name_first))
        self.assertEqual(user.name_first, user_from_mapper.name_first)

    def test_update(self):
        user = self.mapper.find(User, MatchCriteria("name", "daniel"))
        replace_email = "test@the.email"
        user.email = replace_email
        self.mapper.update(User, user)
        user = self.mapper.find(User, MatchCriteria("name", "daniel"))
        self.assertEqual(user.email, replace_email)