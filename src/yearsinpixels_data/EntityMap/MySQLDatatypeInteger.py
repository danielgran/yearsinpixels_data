from yearsinpixels_data.EntityMap.Datatype import Datatype


class MySQLDatatypeInteger(Datatype):
    def convert_to_database(self, element):
        is_integer = isinstance(element, int)
        if not is_integer:
            raise Exception("This method can only be called with an integer.")
        return str(element)

    def convert_from_database(self, element):
        pass
