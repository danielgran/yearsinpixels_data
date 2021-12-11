from yearsinpixels_business.Entity.Day import Day

from yearsinpixels_data.Gateway.TestGateway import TestGateway
from yearsinpixels_data.QueryObject.SelectQuery import SelectQuery


class DayMapper:

    def __init__(self, gateway):
        self.gateway = gateway

    def add(self, day):
        if isinstance(self.gateway, TestGateway):
            self.gateway.items.append(day)
        self.gateway.create_entity(day)

    def find(self, day):
        pass

    def find_all_from_user(self, user, criteria):
        if isinstance(self.gateway, TestGateway):
            return self.gateway.read_all_entities(user)
        select_query = SelectQuery(Day)
        select_query.add_criteria(criteria)
        return self.gateway.read_all_entities(select_query)

    def update(self, user):
        pass

    def remove(self, day):
        pass
