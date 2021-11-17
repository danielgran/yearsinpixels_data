import unittest

from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria
from yearsinpixels_data.QueryObject.QueryObject import QueryObject


class QueryObjectTest(unittest.TestCase):
    def setUp(self):
        self.queryObject = QueryObject()


    def test_is_there(self):
        self.assertIsNotNone(QueryObject)


    def test_add_criteria(self):
        criteria = Criteria.matches("user", "daniel")
        self.queryObject.addCriteria(criteria)
        self.assertTrue(criteria in self.queryObject.criteria)

    def test_print_query(self):
        criteria = Criteria.matches("user", "daniel")
        self.queryObject.addCriteria(criteria)
        generated_sql = self.queryObject.generate_sql()
        self.assertEqual("SELECT * FROM user WHERE `user` = 'daniel';", generated_sql)
