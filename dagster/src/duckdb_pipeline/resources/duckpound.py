class SQL:
    def __init__(self, sql, **bindings):
        self.sql = sql
        self.bindings = bindings
