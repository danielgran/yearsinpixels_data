from yearsinpixels_data.EntityMap.Datatype import Datatype


class DatatypeDate(Datatype):
    def convert_to_database(self, element):
        return f"{element.year}-{element.month}-{element.day}"

    def convert_from_database(self, element):
        return element
