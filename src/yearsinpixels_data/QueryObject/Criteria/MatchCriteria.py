from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria


class MatchCriteria(Criteria):
    def __init__(self, field, value):
        self.operator = "="
        super(MatchCriteria, self).__init__(field, value)

    def generate_sql(self):
        return f"`{self.field}` {self.operator} '{self.value}'";
