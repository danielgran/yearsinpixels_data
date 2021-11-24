import unittest

from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.EntityMap.ConcreteEntityMapFactory import ConcreteEntityMapFactory


class Day:
    pass


class ConcreteMapFactoryTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(ConcreteEntityMapFactory)

    def test_has_methods(self):
        self.assertIsNotNone(ConcreteEntityMapFactory.construct)

    def test_behaviour(self):
        to_test=[User]

        for entity in to_test:
            entity_object = entity()
            entity_map = ConcreteEntityMapFactory.construct(entity_object)
            self.assertIsNotNone(entity_map)
