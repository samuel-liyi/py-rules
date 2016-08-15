from rules.rule_base import BaseRule


class NaiveRule(BaseRule):
    def execute(self, x, mapping):
        return x[mapping['x']].max() <= self.params['max_v']

    def is_manual_rule(self):
        return True
