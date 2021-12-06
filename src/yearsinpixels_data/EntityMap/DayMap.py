from yearsinpixels_data.EntityMap.Datapair import Datapair
from yearsinpixels_data.EntityMap.DatatypeDate import DatatypeDate
from yearsinpixels_data.EntityMap.DatatypeInteger import DatatypeInteger
from yearsinpixels_data.EntityMap.DatatypeString import DatatypeString
from yearsinpixels_data.EntityMap.EntityMap import EntityMap


class DayMap(EntityMap):

    def get_common_name(self):
        return "day"

    def get_primary_identifier_field(self):
        return None

    @property
    def id_user(self):
        return Datapair(DatatypeInteger, "id_user")

    @property
    def date(self):
        return Datapair(DatatypeDate, "date")

    @property
    def title(self):
        return Datapair(DatatypeString, "title")

    @property
    def notes(self):
        return Datapair(DatatypeString, "notes")
