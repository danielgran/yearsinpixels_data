import unittest
import uuid
from datetime import datetime
from hashlib import md5

from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.Gateway.MySQLGateway import MySQLGateway
from yearsinpixels_data.Mapper.UserMapper import UserMapper
from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria


class UserMapperWithMySQLGatewayTest(unittest.TestCase):
    @staticmethod
    def hash_entity(entity):
        string = ""
        for field in dir(entity):
            if field.startswith("_"): continue
            string += field + str(getattr(entity, field))
        return md5(bytes(string, encoding='utf8')).hexdigest()

    def setUp(self):
        gateway = MySQLGateway(username='root', password='somepass', database='yearsinpixels')
        gateway.connect()
        self.usermapper = UserMapper(gateway)

    def test_interaction(self):
        user = User()
        user.email = str(uuid.uuid4())
        # replace microseconds from cache user
        for field in dir(user):
            if isinstance(getattr(user, field), datetime):
                setattr(user, field, getattr(user, field).replace(microsecond=0))

        self.usermapper.add(user)
        user_from_database = self.usermapper.find(Criteria.matches("guid", user.guid))
        self.assertTrue(self.hash_entity(user) == self.hash_entity(user_from_database))

    def test_update(self):
        user = User()
        user.email = str(uuid.uuid4())
        # replace microseconds from cache user
        for field in dir(user):
            if isinstance(getattr(user, field), datetime):
                setattr(user, field, getattr(user, field).replace(microsecond=0))

        self.usermapper.add(user)

        user.email = f"new-email-from-UserMapperWithMySQLGatewayTest-{uuid.uuid4()}"

        self.usermapper.update(user)
        user_from_database = self.usermapper.find(Criteria.matches("guid", user.guid))
        self.assertTrue(self.hash_entity(user) == self.hash_entity(user_from_database))



