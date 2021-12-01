from yearsinpixels_data.EntityMap.DatatypeBoolean import DatatypeBoolean


class MySQLDatatypeBoolean(DatatypeBoolean):
    def convert_to_database(self, boolean):
        is_bool = isinstance(boolean, bool)
        if not is_bool:
            raise Exception("This method can only be called with a boolean.")
        # Safe - ing
        if boolean:
            return '1'
        if not boolean:
            return '0'

    def convert_from_database(self, element):
        is_integer = isinstance(element, int)
        if not is_integer:
            raise Exception("This method can only be called with a boolean.")
        if element != 0 and element != 1:
            raise Exception("This method can only be called with proper integer numbers.")

        if element == 1: return True
        if element == 0: return False
