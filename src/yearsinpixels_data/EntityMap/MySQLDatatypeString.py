from yearsinpixels_data.EntityMap.DatatypeString import DatatypeString


class MySQLDatatypeString(DatatypeString):
    def convert_to_database(self, element):
        is_integer = isinstance(element, str)
        if not is_integer:
            raise Exception("This method can only be called with an integer.")
        # Safe - ing
        return str(element)

    def convert_from_database(self, element):
        pass
