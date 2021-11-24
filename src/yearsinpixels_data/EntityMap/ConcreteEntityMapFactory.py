from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.EntityMap.UserMap import UserMap


class ConcreteEntityMapFactory:

    @staticmethod
    def construct(classtype):
        if type(classtype) is User:
            return UserMap()