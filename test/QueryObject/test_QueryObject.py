import unittest
from abc import ABC

from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria
from yearsinpixels_data.QueryObject.QueryObject import QueryObject



class TestProcedureQueryClass(QueryObject):
    def generate_sql(self):
        pass

class QueryObjectTest(unittest.TestCase):
    def setUp(self):
        self.queryObject = TestProcedureQueryClass()

    def test_is_there(self):
        self.assertIsNotNone(QueryObject)

    def test_is_abstract(self):
        self.assertTrue(issubclass(QueryObject, ABC))

    def test_method_existence(self):
        self.assertIsNotNone(QueryObject.generate_sql)

    def test_add_criteria(self):
        criteria = Criteria.matches("user", "daniel")
        self.queryObject.add_criteria(criteria)
        self.assertTrue(criteria in self.queryObject.criteria)



