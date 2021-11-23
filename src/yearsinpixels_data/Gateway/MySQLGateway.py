from yearsinpixels_business.Entity.Entity import Entity

from yearsinpixels_data.Gateway.Gateway import Gateway


class MySQLGateway(Gateway):
    def create_entity(self, entity):
        pass

    def read_entity(self, entity, criteria=None) -> Entity:
        pass

    def update_entity(self, entity):
        pass

    def delete_entity(self, entity):
        pass

