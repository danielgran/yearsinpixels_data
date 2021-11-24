import unittest

from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.EntityMap.EntityRegistry import EntityRegistry


class EntityRegistryTest(unittest.TestCase):
    def test_is_there_and_is_abstract(self):
        self.assertIsNotNone(EntityRegistry)

    def test_meta(self):
        self.assertIsNotNone(EntityRegistry.get_common_name_from_class)

    def test_registry_entities(self):
        name = EntityRegistry.get_common_name_from_class(User)
        self.assertTrue(isinstance(name, str) and len(name) > 0)