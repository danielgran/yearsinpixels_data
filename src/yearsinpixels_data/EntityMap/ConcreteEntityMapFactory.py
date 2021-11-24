from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.EntityMap.UserMap import UserMap


class ConcreteEntityMapFactory:

    @staticmethod
    def construct(classtype):
        print(type(classtype))
        if classtype is User:
            return UserMap()