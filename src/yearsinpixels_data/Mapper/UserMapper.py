from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.Gateway.TestGateway import TestGateway
from yearsinpixels_data.QueryObject.SelectQuery import SelectQuery

class UserMapper:

    def __init__(self, gateway):
        self.gateway = gateway

    def add(self, entity):
        if isinstance(self.gateway, TestGateway):
            self.gateway.items.append(entity)
        self.gateway.create_entity(entity)

    def find(self, criteria):
        if isinstance(self.gateway, TestGateway):
            return self.gateway.read_entity(None, criteria)
        select_query = SelectQuery(User)
        select_query.add_criteria(criteria)
        return self.gateway.read_entity(select_query)

    def update(self, entity):
        if isinstance(self.gateway, TestGateway):
            self.gateway.update_entity(entity)
        self.gateway.update_entity(entity)

    def remove(self, entity):
        if isinstance(self.gateway, TestGateway):
            self.gateway.delete_entity(entity)
