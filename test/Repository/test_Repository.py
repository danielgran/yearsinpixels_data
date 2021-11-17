import unittest

from yearsinpixels_data.Repository.Repository import Repository


class RepositoryTest(unittest.TestCase):

    def test_is_there(self):
        self.assertIsNotNone(Repository)

    def test_method_integrity(self):
        self.assertIsNotNone(Repository.initialize)
        self.assertIsNotNone(Repository.create)
        self.assertIsNotNone(Repository.read)
        self.assertIsNotNone(Repository.update)
        self.assertIsNotNone(Repository.delete)
