from abc import ABCMeta, abstractmethod


class BaseRule(object):
    __metaclass__ = ABCMeta

    # TODO make sure rules name is unique
    def __init__(self, name, mapping, **params):
        self.name = name
        self.params = params
        self.args = []
        self.bind(mapping)

    def rule_name(self):
        return self.name

    def list_arguments(self):
        return self.args

    def bind(self, arg_map):
        for arg in self.args:
            if arg not in arg_map:
                raise AttributeError("%s is not provided." % arg)
            setattr(self, arg, arg_map[arg])

    # TODO rule data validity  check
    @abstractmethod
    def execute(self):
        pass


