class Criteria:
    def __init__(self, field, value, operator=None):
        if operator is not None:
            self.operator = operator
        self.field = field
        self.value = value

    def generateSQL(self):
        pass

    @staticmethod
    def matches(field, value):
        from yearsinpixels_data.QueryObject.Criteria.MatchCriteria import MatchCriteria
        match_criteria = MatchCriteria(field, value)
        return match_criteria


