from yearsinpixels_data.EntityMap.EntityMap import EntityMap


class UserMap(EntityMap):
    def get_common_name(self):
        return "user"

    @property
    def email(self):
        return "email"

    @property
    def email_verified(self):
        return "email_verified"

    @property
    def name_first(self):
        return "name_first"

    @property
    def name_last(self):
        return "name_last"

    @property
    def gender(self):
        return "gender"

    @property
    def password(self):
        return "password"

    @property
    def password_lastupdate(self):
        return "password_lastupdate"

    @property
    def enabled(self):
        return "enabled"

    @property
    def twofatoken(self):
        return "twofatoken"

    @property
    def last_login(self):
        return "last_login"

    @property
    def modified(self):
        return "modified"

    @property
    def created(self):
        return "created"

