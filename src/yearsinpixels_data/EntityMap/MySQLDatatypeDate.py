from datetime import date

from yearsinpixels_data.EntityMap.DatatypeDate import DatatypeDate


class MySQLDatatypeDate(DatatypeDate):
    def convert_to_database(self, element):
        is_date = isinstance(element, date)
        if not is_date:
            raise Exception("This method can only be called with a date.")
        return f"{element.year}-{element.month}-{element.day}"

    def convert_from_database(self, element):
        return element
