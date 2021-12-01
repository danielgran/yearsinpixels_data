from yearsinpixels_data.EntityMap.DatatypeString import DatatypeString


class MySQLDatatypeString(DatatypeString):
    def convert_to_database(self, element):
        is_string = isinstance(element, str)
        if not is_string:
            raise Exception("This method can only be called with a string.")
        # Safe - ing
        return str(element)

    def convert_from_database(self, element):
        return element

