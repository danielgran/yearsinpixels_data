from yearsinpixels_data.EntityMap.Datapair import Datapair
from yearsinpixels_data.EntityMap.Datatype import Datatype
from yearsinpixels_data.EntityMap.DatatypeBoolean import DatatypeBoolean
from yearsinpixels_data.EntityMap.DatatypeDatetime import DatatypeDatetime
from yearsinpixels_data.EntityMap.DatatypeInteger import DatatypeInteger
from yearsinpixels_data.EntityMap.DatatypeString import DatatypeString
from yearsinpixels_data.EntityMap.EntityMap import EntityMap



class UserMap(EntityMap):
    def get_common_name(self):
        return "user"

    @property
    def guid(self):
        return Datapair(DatatypeString, "guid")

    @property
    def email(self):
        return Datapair(DatatypeString, "email")

    @property
    def email_verified(self):
        return Datapair(DatatypeBoolean, "email_verified")

    @property
    def name_first(self):
        return Datapair(DatatypeString, "name_first")

    @property
    def name_last(self):
        return Datapair(DatatypeString, "name_last")

    @property
    def password(self):
        return Datapair(DatatypeString, "password")

    @property
    def password_last_update(self):
        return Datapair(DatatypeDatetime, "password_last_update")

    @property
    def enabled(self):
        return Datapair(DatatypeBoolean, "enabled")

    @property
    def twofatoken(self):
        return Datapair(DatatypeString, "twofatoken")

    @property
    def login_last(self):
        return Datapair(DatatypeDatetime, "login_last")

    @property
    def modified(self):
        return Datapair(DatatypeDatetime, "modified")

    @property
    def created(self):
        return Datapair(DatatypeDatetime, "created")
