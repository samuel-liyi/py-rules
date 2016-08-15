from abc import ABCMeta, abstractmethod


class BaseRule(object):
    __metaclass__ = ABCMeta

    # TODO make sure rules name is unique
    def __init__(self, name, params, is_manual=True):
        self.is_manual = is_manual
        self.name = name
        self.params = params

    # TODO rule data validity  check
    @abstractmethod
    def execute(self, data, mapping, params):
        pass

    @abstractmethod
    def is_manual_rule(self):
        return self.is_manual

    def rule_name(self):
        return self.name
