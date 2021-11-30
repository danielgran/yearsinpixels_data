from yearsinpixels_data.EntityMap.DatatypeDatetime import DatatypeDatetime


class MySQLDatatypeDatetime(DatatypeDatetime):
    def convert_to_database(self, element):
        is_integer = isinstance(element, float)
        if not is_integer:
            raise Exception("This method can only be called with a datetime.")
        return str(int(element))

    def convert_from_database(self, element):
        pass
