from yearsinpixels_business.Entity.Mood import Mood
from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.Gateway.TestGateway import TestGateway
from yearsinpixels_data.QueryObject.SelectQuery import SelectQuery

class MoodMapper:

    def __init__(self, gateway):
        self.gateway = gateway

    def add(self, mood):
        self.gateway.items.append(mood)

    def find(self, user):
        pass

    def find_all(self):
        if isinstance(self.gateway, TestGateway):
            return self.gateway.read_all_entities(User)
        select_query = SelectQuery(Mood)
        return self.gateway.read_entity(select_query)

    def update(self, user, day):
        pass

    def remove(self, user, day):
        pass
