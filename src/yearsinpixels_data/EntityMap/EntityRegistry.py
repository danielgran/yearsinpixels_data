from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.EntityMap.UserMap import UserMap


class EntityRegistry:

    @staticmethod
    def get_common_name_from_entity(entity):
        if entity is User:
            user_map = UserMap()
            return user_map.get_common_name()