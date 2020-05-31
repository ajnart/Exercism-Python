from collections import defaultdict


class School(object):
    def __init__(self):
        self.db = defaultdict(set)

    def grade(self, n):
        return sorted(list(self.db[n])) or []

    def add_student(self, name, grade):
        self.db[grade].add(name)

    def roster(self):
        return [name for k, v in sorted(self.db.items()) for name in sorted(v)]