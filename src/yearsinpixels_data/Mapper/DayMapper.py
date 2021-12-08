from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.Gateway.TestGateway import TestGateway
from yearsinpixels_data.QueryObject.SelectQuery import SelectQuery


class DayMapper:

    def __init__(self, gateway):
        self.gateway = gateway

    def add(self, user, day):
        if isinstance(self.gateway, TestGateway):
            self.gateway.items.append((user, day))

    def find(self, user):
        pass

    def find_all(self, user, criteria):
        if isinstance(self.gateway, TestGateway):
            return self.gateway.read_all_entities(user)
        select_query = SelectQuery(User)
        select_query.add_criteria(criteria)
        return self.gateway.read_entity(select_query)

    def update(self, user, day):
        pass

    def remove(self, user, day):
        pass
