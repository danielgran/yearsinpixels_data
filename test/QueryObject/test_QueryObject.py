import unittest

from yearsinpixels_data.QueryObject import QueryObject



class QueryObjectTest(unittest.TestCase):
    def setUp(self):
        self.queryObject = QueryObject()


    def test_is_there(self):
        self.assertIsNotNone(QueryObject)


    #def test_criteria(self):
        #self.queryObject.addCriteria(Criteria.matches("daniel", "user"))