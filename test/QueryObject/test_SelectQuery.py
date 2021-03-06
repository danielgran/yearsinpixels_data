import unittest

from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria
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
        with self.assertRaises(Exception) as context:
            SelectQuery(SelectQueryTest)  # Random Class should throw error, only entities.

    def test_print_query(self):
        self.queryObject.add_criteria(Criteria.matches("guid", "some-random-guid"))
        self.queryObject.add_criteria(Criteria.matches("name", "pete"))
        self.queryObject.add_criteria(Criteria.matches("krawatte", "keine"))
        generated_sql = self.queryObject.generate_sql()
        self.assertEqual(
            "SELECT created, email, email_verified, enabled, guid, id, login_last, modified, name_first, name_last, "
            "password, password_last_update, twofatoken "
            "FROM user "
            "WHERE `guid` = %(guid)s AND `name` = %(name)s AND `krawatte` = %(krawatte)s",
            generated_sql)

    def test_without_criteria(self):
        sql = self.queryObject.generate_sql()
        self.assertTrue(sql.count("WHERE") == 0)
