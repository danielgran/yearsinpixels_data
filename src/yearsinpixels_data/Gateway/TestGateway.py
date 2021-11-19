from yearsinpixels_data.Gateway.Gateway import Gateway


class TestGateway(Gateway):
    def __init__(self):
        self.items = list()


    def create_entity(self, entity):
        self.items.append(entity)

    def read_entity(self, entity):
        for iter in range(len(self.items)):
            if entity.guid == self.items[iter].guid:
                return self.items[iter]

    def update_entity(self, entity):
        for iter in range(len(self.items)):
            if entity.guid == self.items[iter].guid:
                self.items[iter] = entity

    def delete_entity(self, entity):
        for iter in range(len(self.items)):
            if entity.guid == self.items[iter].guid:
                del(self.items[iter])

