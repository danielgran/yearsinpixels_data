from yearsinpixels_business.Entity.Mood import Mood
from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.Gateway.TestGateway import TestGateway
from yearsinpixels_data.QueryObject.SelectQuery import SelectQuery

class MoodMapper:

    def __init__(self, gateway):
        self.gateway = gateway

    def add(self, mood):
        if (isinstance(self.gateway, TestGateway)):
            self.gateway.items.append(mood)
        self.gateway.create_entity(mood)


    def find(self, user):
        pass

    def find_all(self):
        if isinstance(self.gateway, TestGateway):
            return self.gateway.read_all_entities(User)
        select_query = SelectQuery(Mood)
        return self.gateway.read_all_entities(select_query)

    def update(self, user, day):
        pass

    def remove(self, user, day):
        pass
