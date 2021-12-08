import unittest

from yearsinpixels_business.Entity.Day import Day
from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.Gateway.TestGateway import TestGateway
from yearsinpixels_data.Mapper.DayMapper import DayMapper
from yearsinpixels_data.QueryObject.Criteria.MatchCriteria import MatchCriteria


class DayMapperTest(unittest.TestCase):
    def setUp(self):
        test_gateway = TestGateway()
        self.mapper = DayMapper(test_gateway)

    def test_is_there(self):
        self.assertIsNotNone(DayMapper)

    def test_metadata(self):
        self.assertIsNotNone(self.mapper.gateway)
        self.assertIsNotNone(self.mapper.add)
        self.assertIsNotNone(self.mapper.find_all)
        self.assertIsNotNone(self.mapper.update)
        self.assertIsNotNone(self.mapper.remove)

    def test_add(self):
        user = User()
        day = Day()
        self.mapper.add(user, day)

        self.assertTrue((user, day) in self.mapper.gateway.items)

    def test_find(self):
        pass

    def test_find_all(self):
        user = User()
        user.guid = "some-guid"
        day = Day()
        day.title = "some-day"
        self.mapper.gateway.items.append((user, day))
        self.mapper.gateway.items.append((user, day))
        self.mapper.gateway.items.append((user, day))
        criteria = MatchCriteria('guid', user.guid)
        days_from_mapper = self.mapper.find_all(user, criteria)

        self.assertEqual(len(days_from_mapper), 3)

    def test_update(self):
        pass

    def test_remove(self):
        pass
