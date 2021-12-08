import unittest
from hashlib import md5

from yearsinpixels_business.Entity.Mood import Mood

import test
from yearsinpixels_data.Gateway.MySQLGateway import MySQLGateway
from yearsinpixels_data.Mapper.MoodMapper import MoodMapper


@unittest.skipIf(test.disable_mysql_testcase,
                 "MySQL support will not work on this system. Use the 'yearsinpixels_data.Gateway.TestGateway' package.")
class MoodMapperWithMySQLGatewayTest(unittest.TestCase):
    @staticmethod
    def hash_entity(entity):
        string = ""
        for field in dir(entity):
            if field.startswith("_"): continue
            if field.startswith("id"): continue
            string += field + str(getattr(entity, field))
        return md5(bytes(string, encoding='utf8')).hexdigest()

    def setUp(self):
        gateway = MySQLGateway(username='root', password='somepass', database='yearsinpixels')
        gateway.connect()
        self.moodmapper = MoodMapper(gateway)

    def test_add_and_find_all(self):
        mood = Mood()

        self.moodmapper.add(mood)

        moods_from_database = self.moodmapper.find_all()

        local_mood_hash = self.hash_entity(mood)
        for single_mood_from_database in moods_from_database:
            if self.hash_entity(single_mood_from_database) == local_mood_hash:
                return
        self.fail()
