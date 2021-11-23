from yearsinpixels_data.Gateway.TestGateway import TestGateway


class UserMapper:

    def __init__(self, gateway):
        self.gateway = gateway

    def add(self, entity):
        if isinstance(self.gateway, TestGateway):
            self.gateway.items.append(entity)

    def find(self, criteria):
        if isinstance(self.gateway, TestGateway):
            return self.gateway.read_entity(None, criteria)

    def update(self, entity):
        if isinstance(self.gateway, TestGateway):
            self.gateway.update_entity(entity)

    def remove(self, entity):
        if isinstance(self.gateway, TestGateway):
            self.gateway.delete_entity(entity)
