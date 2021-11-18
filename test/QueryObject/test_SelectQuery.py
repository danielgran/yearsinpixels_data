import unittest

from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria
from yearsinpixels_data.QueryObject.QueryObject import QueryObject
from yearsinpixels_data.QueryObject.SelectQuery import SelectQuery


class SelectQueryTest(unittest.TestCase):
    def setUp(self):
        self.queryObject = SelectQuery()

    def test_is_there(self):
        self.assertIsNotNone(SelectQuery)

    def test_is_query_object(self):
        self.assertTrue(issubclass(SelectQuery, QueryObject))

    def test_print_query(self):
        criteria = Criteria.matches("user", "daniel")
        self.queryObject.addCriteria(criteria)
        generated_sql = self.queryObject.generate_sql()
        self.assertEqual("SELECT * FROM user WHERE `user` = 'daniel';", generated_sql)

