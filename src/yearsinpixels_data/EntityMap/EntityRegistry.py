from yearsinpixels_data.EntityMap.ConcreteEntityMapFactory import ConcreteEntityMapFactory


class EntityRegistry:

    @staticmethod
    def get_common_name_from_class(entity_class):
        map = ConcreteEntityMapFactory.construct(entity_class)
        return map.get_common_name()


