import unittest

from yearsinpixels_business.Entity.Day import Day
from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria
from yearsinpixels_data.QueryObject.JoinQuery import JoinQuery
from yearsinpixels_data.QueryObject.QueryObject import QueryObject


class JoinQueryTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(JoinQuery)

    def test_is_query_object(self):
        self.assertTrue(issubclass(JoinQuery, QueryObject))

    def test_constructor(self):
        joinquery = JoinQuery(User, Day)
        self.assertIsNotNone(joinquery.parent_class)
        self.assertIsNotNone(joinquery.child_class)

    def test_generate_sql(self):
        joinquery = JoinQuery(User, Day)
        self.assertTrue(joinquery)

    def test_generate_sql_with_criteria(self):
        joinquery = JoinQuery(User, Day)
        joinquery.add_criteria(Criteria.matches("guid", "some-guid"))
        generated_string = joinquery.generate_sql()
        self.assertTrue(generated_string.endswith("'"))

    def test_generate_sql_with_criteria_with_no_criteria(self):
        joinquery = JoinQuery(User, Day)
        generated_string = joinquery.generate_sql()
        self.assertTrue(not generated_string.endswith("WHERE "))
