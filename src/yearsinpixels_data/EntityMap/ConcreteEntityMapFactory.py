from yearsinpixels_business.Entity.Day import Day
from yearsinpixels_business.Entity.Mood import Mood
from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.EntityMap.DayMap import DayMap
from yearsinpixels_data.EntityMap.MoodMap import MoodMap
from yearsinpixels_data.EntityMap.UserMap import UserMap


class ConcreteEntityMapFactory:

    @staticmethod
    def construct(classtype):
        if classtype is User:
            return UserMap()
        if classtype is Day:
            return DayMap()
        if classtype is Mood:
            return MoodMap()
        raise Exception("Classtype unkown.")
