import unittest

from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria
from yearsinpixels_data.QueryObject.QueryObject import QueryObject
from yearsinpixels_data.QueryObject.UpdateQuery import UpdateQuery


class UpdateQueryTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(UpdateQuery)

    def test_class_meta(self):
        self.assertTrue(issubclass(UpdateQuery, QueryObject))

    def test_creation(self):
        self.assertIsNotNone(UpdateQuery(User))

    def test_fail_safe_creation(self):
        arg = User()
        self.assertRaises(Exception, UpdateQuery, arg)

    def test_set_update_data(self):
        query = UpdateQuery(User)
        user = User()
        query.set_update_object(user)

    def test_failsafe_update_object(self):
        query = UpdateQuery(User)
        some_string = "Edsger W. Dijkstra"
        self.assertRaises(Exception, query.set_update_object, User)
        self.assertRaises(Exception, query.set_update_object, some_string)

    def test_simple_query(self):
        update_query = UpdateQuery(User)
        user = User()
        user.name_first = "Edsger"
        user.name_last = "Dijkstra"
        update_query.set_update_object(user)

        update_query.add_criteria(Criteria.matches("guid", "some-guid"))
        generated_sql = update_query.generate_sql()
