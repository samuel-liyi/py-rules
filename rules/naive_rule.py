from rules.rule_base import BaseRule


class NaiveRule(BaseRule):
    def __init__(self, name, mapping, param_max=0):
        self.name = name
        self.simple_list = None
        self.args = ['simple_list']
        self.bind(mapping)
        self.param_max = param_max

    def execute(self):
        for arg in self.args:
            if not hasattr(self, arg):
                raise AttributeError("%arg not specified, please run `bind` first " % arg)
        return self.simple_list.max() <= self.param_max
