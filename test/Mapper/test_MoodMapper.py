import unittest
import uuid

from yearsinpixels_business.Entity.Mood import Mood

from yearsinpixels_data.Gateway.TestGateway import TestGateway
from yearsinpixels_data.Mapper.MoodMapper import MoodMapper


class MoodMapperTest(unittest.TestCase):
    def setUp(self):
        test_gateway = TestGateway()
        self.mapper = MoodMapper(test_gateway)

    def test_is_there(self):
        self.assertIsNotNone(MoodMapper)

    def test_metadata(self):
        self.assertIsNotNone(self.mapper.gateway)
        self.assertIsNotNone(self.mapper.add)
        self.assertIsNotNone(self.mapper.find)
        self.assertIsNotNone(self.mapper.find_all)
        self.assertIsNotNone(self.mapper.update)
        self.assertIsNotNone(self.mapper.remove)

    def test_add(self):
        mood = Mood()
        mood.title = str(uuid.uuid4())
        self.mapper.add(mood)

        self.assertTrue(mood in self.mapper.gateway.items)

    def test_find(self):
        pass

    def test_find_all(self):
        count = 100
        for i in range(count):
            mood = Mood()
            mood.title = str(i)
            self.mapper.gateway.items.append((Mood, mood))

        moods_from_mapper = self.mapper.find_all()

        self.assertEqual(len(moods_from_mapper), count)

    def test_update(self):
        pass

    def test_remove(self):
        pass
