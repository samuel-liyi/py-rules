from rules.rule_base import BaseRule


class Manager(object):
    def __init__(self, rules=None):
        if rules is None:
            self.rules = []
            self.results = {}

    def add_rule(self, r):
        if not isinstance(r, BaseRule):
            raise TypeError("not rule instance,error!")
            return
        if r in self.rules:
            return self
        self.rules.append(r)
        return self

    def execute(self):
        for r in self.rules:
            res = r.execute()
            self.results[r] = res
            print("the result of rule #{:s}# is {:s}".format(r.rule_name(), str(res)))
        return self.results[r]





