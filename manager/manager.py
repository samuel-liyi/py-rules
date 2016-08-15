from rules.rule_base import BaseRule


class Manager(object):
    def __init__(self, data, rules=None):
        if rules is None:
            self.rules = []
            self.rule_mapping = {}
            self.results = {}
        self.data = data

    def add_rule(self, r, mapping):
        if not isinstance(r, BaseRule):
            print("not rule instance,error!")
            return
        if r in self.rules:
            return self
        self.rules.append(r)
        self.rule_mapping[r] = mapping
        return self

    def execute(self):
        for r in self.rules:
            res = r.execute(self.data, self.rule_mapping[r])
            self.results[r] = res
            print("the result of rule {:s} is {:b}".format(r.rule_name(), res))
        return self.results[r]





