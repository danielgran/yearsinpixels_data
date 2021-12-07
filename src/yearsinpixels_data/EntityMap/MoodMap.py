from yearsinpixels_data.EntityMap.Datapair import Datapair
from yearsinpixels_data.EntityMap.DatatypeDate import DatatypeDate
from yearsinpixels_data.EntityMap.DatatypeInteger import DatatypeInteger
from yearsinpixels_data.EntityMap.DatatypeString import DatatypeString
from yearsinpixels_data.EntityMap.EntityMap import EntityMap


class MoodMap(EntityMap):

    def get_common_name(self):
        return "mood"

    def get_primary_identifier_field(self):
        return None

    @property
    def id(self):
        return Datapair(DatatypeInteger, "id")

    @property
    def title(self):
        return Datapair(DatatypeDate, "title")

    @property
    def color(self):
        return Datapair(DatatypeString, "color")
