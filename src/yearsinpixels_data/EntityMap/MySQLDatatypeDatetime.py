from datetime import datetime

from yearsinpixels_data.EntityMap.DatatypeDatetime import DatatypeDatetime



class MySQLDatatypeDatetime(DatatypeDatetime):
    def convert_to_database(self, element):
        is_time = isinstance(element, datetime)
        if not is_time:
            raise Exception("This method can only be called with a datetime.")
        time = element.strftime('%Y-%m-%d %H:%M:%S')
        return str(time)

    def convert_from_database(self, date_time):
        if not isinstance(date_time, datetime): raise Exception
        return date_time
