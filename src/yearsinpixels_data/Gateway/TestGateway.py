from yearsinpixels_data.Gateway.Gateway import Gateway


class TestGateway(Gateway):
    def __init__(self):
        self.items = list()


    def create_entity(self, entity):
        self.items.append(entity)

    def read_entity(self, entity, criteria=None):
        to_return = None
        if criteria is not None:
            if criteria.operator == "=":
                for iterator in range(len(self.items)):
                    current_item_member = getattr(self.items[iterator], criteria.field)
                    if current_item_member == criteria.value:
                        to_return = self.items[iterator]
                        break
        else:
            for iterator in range(len(self.items)):
                if entity.guid == self.items[iterator].guid:
                    to_return = self.items[iterator]
        return to_return

    def update_entity(self, entity):
        for iter in range(len(self.items)):
            if entity.guid == self.items[iter].guid:
                self.items[iter] = entity

    def delete_entity(self, entity):
        for iter in range(len(self.items)):
            if entity.guid == self.items[iter].guid:
                del(self.items[iter])

