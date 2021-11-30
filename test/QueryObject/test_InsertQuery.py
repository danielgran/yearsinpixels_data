import unittest

from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.QueryObject.InsertQuery import InsertQuery
from yearsinpixels_data.QueryObject.QueryObject import QueryObject


class CreateQueryTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(InsertQuery)

    def test_integrity(self):
        self.assertTrue(issubclass(InsertQuery, QueryObject))

    def test_creation(self):
        user = User()
        self.assertIsNotNone(InsertQuery(user))

    def test_sql_generation(self):
        user = User()
        query = InsertQuery(user).generate_sql()


        self.assertTrue(query.startswith("INSERT"))
