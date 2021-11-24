import unittest

from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.EntityMap.ConcreteEntityMapFactory import ConcreteEntityMapFactory


class ConcreteMapFactoryTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(ConcreteEntityMapFactory)

    def test_has_methods(self):
        self.assertIsNotNone(ConcreteEntityMapFactory.construct)

    def test_behaviour(self):
        classes=[User]

        for entity_class in classes:
            entity_map = ConcreteEntityMapFactory.construct(entity_class)
            self.assertIsNotNone(entity_map)
