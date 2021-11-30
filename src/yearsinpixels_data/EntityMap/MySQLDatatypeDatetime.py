from datetime import datetime

from yearsinpixels_data.EntityMap.DatatypeDatetime import DatatypeDatetime



class MySQLDatatypeDatetime(DatatypeDatetime):
    def convert_to_database(self, element):
        is_time = isinstance(element, float)
        if not is_time:
            raise Exception("This method can only be called with a datetime.")
        time = datetime.utcfromtimestamp(int(element)).strftime('%Y-%m-%d %H:%M:%S')
        return str(time)

    def convert_from_database(self, element):
        pass
