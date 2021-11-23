from yearsinpixels_business.Entity.Entity import Entity

from yearsinpixels_data.Gateway.TestGateway import TestGateway
from yearsinpixels_data.QueryObject.SelectQuery import SelectQuery


class Mapper:

    def __init__(self, gateway):
        self.gateway = gateway

    def add(self, entity):
        if isinstance(self.gateway, TestGateway):
            self.gateway.items.append(entity)

    def find(self, criteria):

        if isinstance(self.gateway, TestGateway):
            return self.gateway.read_entity(None, criteria)
        else:
        # translate criteria in usable stuff
            select_query = SelectQuery()
            select_query.addCriteria(criteria)
            sql = select_query.generate_sql()
            #return_val = gateway.execsql(sql)
        #return_val = map_data(return_val)
        # it depends solely on the gateway how to gather data, its not always sql
        # i could either work with some basic switch case functionality here or i could make in polymorph

    def update(self, entity):
        if isinstance(self.gateway, TestGateway):
            self.gateway.update_entity(entity)

    def remove(self, entity):
        if isinstance(self.gateway, TestGateway):
            self.gateway.delete_entity(entity)
