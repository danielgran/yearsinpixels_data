from yearsinpixels_data.EntityMap.DatatypeBoolean import DatatypeBoolean


class MySQLDatatypeBoolean(DatatypeBoolean):
    def convert_to_database(self, boolean):
        is_integer = isinstance(boolean, bool)
        if not is_integer:
            raise Exception("This method can only be called with a boolean.")
        # Safe - ing
        if boolean:
            return '1'
        if not boolean:
            return '0'

    def convert_from_database(self, element):
        pass
