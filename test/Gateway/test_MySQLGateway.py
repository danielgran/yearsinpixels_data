import unittest
import uuid
from datetime import date, datetime, timedelta
from hashlib import md5

from yearsinpixels_business.Entity.Day import Day
from yearsinpixels_business.Entity.Mood import Mood
from yearsinpixels_business.Entity.User import User

import test
from yearsinpixels_data.Database.MySQLConnection import MySQLConnection
from yearsinpixels_data.Gateway.Gateway import Gateway
from yearsinpixels_data.Gateway.MySQLGateway import MySQLGateway
from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria
from yearsinpixels_data.QueryObject.Criteria.MatchCriteria import MatchCriteria
from yearsinpixels_data.QueryObject.SelectQuery import SelectQuery


@unittest.skipIf(test.disable_mysql_testcase,
                 "MySQL support will not work on this system. Use the 'yearsinpixels_data.Gateway.TestGateway' package.")
class MySQLGatewayTest(unittest.TestCase):
    @staticmethod
    def hash_entity(entity):
        string = ""
        for field in dir(entity):
            if field.startswith("_"): continue
            if field.startswith("id"): continue
            if isinstance(getattr(entity, field), str):
                string += field + getattr(entity, field)
            else:
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

    def test_is_there(self):
        self.assertIsNotNone(MySQLGateway)

    def test_is_gateway(self):
        self.assertTrue(issubclass(MySQLGateway, Gateway))

    def test_create_entity(self):
        user = User()
        user.email = str(uuid.uuid4())
        self.gateway.create_entity(user)

    def test_create_foreign_key_entity(self):
        user = User()
        user.email = str(uuid.uuid4())
        self.gateway.create_entity(user)
        select_query = SelectQuery(User)
        select_query.add_criteria(MatchCriteria("guid", user.guid))
        user = self.gateway.read_entity(select_query)

        mood = Mood()
        mood.title = str(uuid.uuid4())
        self.gateway.create_entity(mood)
        select_query = SelectQuery(Mood)
        select_query.add_criteria(MatchCriteria("title", mood.title))
        mood = self.gateway.read_entity(select_query)

        day = Day()
        day.title = "some-day"
        day.id_user = user.id
        day.id_mood1 = mood.id
        self.gateway.create_entity(day)

        select_query = SelectQuery(Day)
        select_query.add_criteria(Criteria.matches("id_user", user.id))
        day_from_database = self.gateway.read_entity(select_query)
        local_hash = self.hash_entity(day)
        database_hash = self.hash_entity(day_from_database)
        self.assertEqual(local_hash, database_hash)

    def test_read_entity(self):
        user = User()

        for field in dir(user):
            if isinstance(getattr(user, field), datetime):
                setattr(user, field, getattr(user, field).replace(microsecond=0))

        user.email = str(uuid.uuid4())
        self.gateway.create_entity(user)

        select_query = SelectQuery(User)
        select_query.add_criteria(MatchCriteria("guid", user.guid))
        user_from_database = self.gateway.read_entity(select_query)

        hash_entity_local = self.hash_entity(user)
        hash_entity_database = self.hash_entity(user_from_database)
        self.assertTrue(hash_entity_local == hash_entity_database)

    def test_read_all_entites(self):
        mood = Mood()
        self.gateway.create_entity(mood)
        user = User()
        user.email = str(uuid.uuid4())
        self.gateway.create_entity(user)
        select_query = SelectQuery(User)
        select_query.add_criteria(MatchCriteria("guid", user.guid))
        user = self.gateway.read_entity(select_query)
        count = 100
        for i in range(count):
            day = Day()
            day.title = str(i)
            day.id_mood1 = 1
            day.id_user = user.id
            day.date = date.today() + timedelta(days=i)
            self.gateway.create_entity(day)

        select_query = SelectQuery(Day)
        select_query.add_criteria(Criteria.matches("id_user", user.id))
        days = self.gateway.read_all_entities(select_query)
        self.assertEqual(len(days), count)

    def test_update_entity(self):
        user = User()
        unique = uuid.uuid4()
        user.email = f"this.email@didnotgetupdat.edu-{unique}"

        for field in dir(user):
            if isinstance(getattr(user, field), datetime):
                setattr(user, field, getattr(user, field).replace(microsecond=0))
        self.gateway.create_entity(user)

        user.email = f"this.email@was.updated-{unique}"
        self.gateway.update_entity(user)

        select = SelectQuery(User)
        select.add_criteria(Criteria.matches("guid", user.guid))
        user_from_database = self.gateway.read_entity(select)

        hash_entity_database = self.hash_entity(user_from_database)
        hash_entity_local = self.hash_entity(user)

        self.assertTrue(hash_entity_local == hash_entity_database)

    def test_delete_entity(self):
        pass
