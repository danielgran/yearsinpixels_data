import unittest

from yearsinpixels_business.Entity.Day import Day
from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.Gateway.Gateway import Gateway
from yearsinpixels_data.Gateway.TestGateway import TestGateway
from yearsinpixels_data.QueryObject.Criteria.MatchCriteria import MatchCriteria


class TestGatewayTest(unittest.TestCase):
    def setUp(self):
        self.gateway = TestGateway()

    def test_is_there(self):
        self.assertIsNotNone(TestGateway)

    def test_is_gateway(self):
        self.assertTrue(issubclass(TestGateway, Gateway))

    def test_create(self):
        entity = User()
        self.gateway.create_entity(entity)

        self.assertTrue(entity in self.gateway.items)

    def test_read(self):
        entity = User()
        self.gateway.create_entity(entity)

        self.assertTrue(self.gateway.read_entity(entity) == entity, "Can not find added entity.")

    def test_read_all_entites(self):
        user = User()
        day = Day()
        self.gateway.create_entity((user, day))
        self.gateway.create_entity((user, day))
        self.gateway.create_entity((user, day))

        self.assertEqual(len(self.gateway.read_all_entities(user)), 3)



    def test_read_with_meta(self):
        entity = User()
        entity.name_last = "Peter"
        self.gateway.create_entity(entity)
        matchcriteria = MatchCriteria("name_last", entity.name_last)
        entity_from_gateway = self.gateway.read_entity(entity, matchcriteria)

        self.assertEqual(entity.name_last, entity_from_gateway.name_last)

    def test_update(self):
        entity = User()
        self.gateway.create_entity(entity)
        email = "some@testing.email"
        entity.email = email
        self.gateway.update_entity(entity)

        self.assertTrue(self.gateway.read_entity(entity).email == "some@testing.email")

    def test_delete(self):
        entity = User()
        self.gateway.create_entity(entity)
        self.assertTrue(entity in self.gateway.items)
        self.gateway.delete_entity(entity)
        updated_entity = self.gateway.read_entity(entity)

        self.assertIsNone(updated_entity)
