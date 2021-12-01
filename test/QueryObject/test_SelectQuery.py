import unittest

from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria
from yearsinpixels_data.QueryObject.Criteria.MatchCriteria import MatchCriteria
from yearsinpixels_data.QueryObject.QueryObject import QueryObject
from yearsinpixels_data.QueryObject.SelectQuery import SelectQuery


class SelectQueryTest(unittest.TestCase):
    def setUp(self):
        self.queryObject = SelectQuery(User)

    def test_is_there(self):
        self.assertIsNotNone(SelectQuery)

    def test_is_query_object(self):
        self.assertTrue(issubclass(SelectQuery, QueryObject))

    def test_creation(self):
        SelectQuery(User)
        with self.assertRaises(Exception) as ctx:
            SelectQuery(SelectQueryTest) # Random Class should throw error, only entities.

    def test_print_query(self):
        self.queryObject.add_criteria(Criteria.matches("guid", "some-random-guid"))
        self.queryObject.add_criteria(Criteria.matches("name", "pete"))
        self.queryObject.add_criteria(Criteria.matches("krawatte", "keine"))
        generated_sql = self.queryObject.generate_sql()
        self.assertEqual("SELECT * FROM user WHERE `guid` = 'some-random-guid' AND `name` = 'pete' AND `krawatte` = 'keine';", generated_sql)

