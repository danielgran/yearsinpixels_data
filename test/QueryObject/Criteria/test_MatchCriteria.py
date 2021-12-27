import unittest

from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.QueryObject.Criteria.MatchCriteria import MatchCriteria


class MatchCriteriaTest(unittest.TestCase):
    def setUp(self):
        self.criteria = MatchCriteria("field", "value")

    def test_is_there(self):
        self.assertIsNotNone(MatchCriteria)
        self.assertIsNotNone(self.criteria)

    def test_integrity(self):
        self.assertEqual(self.criteria.operator, "=")

    def test_generate_sql(self):
        sql = self.criteria.generate_sql()
        self.assertTrue(isinstance(sql, str))
        self.assertEqual(sql, "`field` = %(field)s")
