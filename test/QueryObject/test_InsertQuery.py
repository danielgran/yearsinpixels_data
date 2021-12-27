import unittest
from datetime import date

from yearsinpixels_business.Entity.Day import Day
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


    def test_sql_generation_with_hidden_id(self):
        day = Day()
        day.date = date(2021, 12, 12)
        day.id_mood1 = 1
        day.id_mood2 = 0
        query = InsertQuery(day).generate_sql()
        self.assertEqual(query, "INSERT INTO day (date, id_mood1, notes, title) VALUES ( %(date)s, %(id_mood1)s, %(notes)s, %(title)s);")
        print(query)

