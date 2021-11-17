import unittest

from yearsinpixels_data.Repository.Repository import Repository
from yearsinpixels_data.Repository.UserRepository import UserRepository


class UserRepositoryTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(UserRepository)

    def test_inheritance(self):
        self.assertTrue(issubclass(UserRepository, Repository))

