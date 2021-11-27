from yearsinpixels_data.EntityMap.DataPair import DataPair
from yearsinpixels_data.EntityMap.Datatype import Datatype
from yearsinpixels_data.EntityMap.EntityMap import EntityMap


class UserMap(EntityMap):
    def get_common_name(self):
        return "user"

    @property
    def guid(self):
        return DataPair(Datatype.STRING, "guid")

    @property
    def email(self):
        return DataPair(Datatype.STRING, "email")

    @property
    def email_verified(self):
        return DataPair(Datatype.BOOLEAN, "email_verified")

    @property
    def name_first(self):
        return DataPair(Datatype.STRING, "name_first")

    @property
    def name_last(self):
        return DataPair(Datatype.STRING, "name_last")

    @property
    def gender(self):
        return DataPair(Datatype.STRING, "gender")

    @property
    def password(self):
        return DataPair(Datatype.STRING, "password")

    @property
    def password_last_update(self):
        return DataPair(Datatype.DATETIME, "password_last_update")

    @property
    def enabled(self):
        return DataPair(Datatype.BOOLEAN, "enabled")

    @property
    def twofatoken(self):
        return DataPair(Datatype.STRING, "twofatoken")

    @property
    def login_last(self):
        return DataPair(Datatype.DATETIME, "login_last")

    @property
    def modified(self):
        return DataPair(Datatype.DATETIME, "modified")

    @property
    def created(self):
        return DataPair(Datatype.DATETIME, "created")
