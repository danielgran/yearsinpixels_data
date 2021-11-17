class QueryObject:
    def __init__(self):
        self.criteria = list()

    def generate_sql(self):
        gen_query = "SELECT * FROM user WHERE "
        iterator = 0
        for criteria in self.criteria:
            gen_query += criteria.generate_sql()
            if iterator + 1 != len(self.criteria):
                gen_query += ", "
            iterator += 1

        gen_query += ";"
        return gen_query

    def addCriteria(self, criteria):
        self.criteria.append(criteria)

