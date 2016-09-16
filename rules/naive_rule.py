from rules.rule_base import BaseRule

class NaiveRule(BaseRule):
    def __init__(self, name, mapping, **params):
        self.name = name
        self.simple_list = None
        self.params = params
        self.args = ['simple_list']
        self.bind(mapping)

    def execute(self):
        for arg in self.args:
            if not hasattr(self, arg):
                raise AttributeError("%arg not specified, please run `bind` first " % arg)
        return self.simple_list.max() <= self.params.get('param_max', 0)
