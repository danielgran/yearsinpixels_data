import random
import unittest
import uuid
from datetime import timedelta
from hashlib import md5

from yearsinpixels_business.Entity.Day import Day
from yearsinpixels_business.Entity.Mood import Mood
from yearsinpixels_business.Entity.User import User

import test
from yearsinpixels_data.Database.MySQLConnection import MySQLConnection
from yearsinpixels_data.Gateway.MySQLGateway import MySQLGateway
from yearsinpixels_data.Mapper.DayMapper import DayMapper
from yearsinpixels_data.Mapper.MoodMapper import MoodMapper
from yearsinpixels_data.Mapper.UserMapper import UserMapper
from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria


@unittest.skipIf(test.disable_mysql_testcase,
                 "MySQL support will not work on this system. Use the 'yearsinpixels_data.Gateway.TestGateway' package.")
class DayMapperWithMySQLGateway(unittest.TestCase):
    @staticmethod
    def hash_entity(entity):
        string = ""
        for field in dir(entity):
            if field.startswith("_"): continue
            if field.startswith("id"): continue
            string += field + str(getattr(entity, field))
        return md5(bytes(string, encoding='utf8')).hexdigest()

    def setUp(self):
        username = "root"
        password = "somepass"
        host = "localhost"
        port = 3306
        database = "yearsinpixels"
        mysqlconnection = MySQLConnection(username=username, password=password, host=host, port=port, database=database)
        mysqlconnection.connect()
        self.gateway = MySQLGateway(mysqlconnection)
        self.daymapper = DayMapper(self.gateway)

    def test_add_and_find_all(self):
        user = User()
        user.email = str(uuid.uuid4())
        user_mapper = UserMapper(self.gateway)
        user_mapper.add(user)
        mood = Mood()
        moodMapper = MoodMapper(self.gateway)
        moodMapper.add(mood)
        day = Day()
        day.date = day.date + timedelta(days=random.randint(0, 1000000))
        day.id_mood1 = 1
        day.id_user = 1
        self.daymapper.add(day)

        days_from_mapper = self.daymapper.find_all_from_user(Criteria.matches('id_user', 1))

        for day in days_from_mapper:
            if day.id_user != 1:
                self.fail()
