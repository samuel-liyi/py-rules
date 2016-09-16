from manager.manager import Manager
from rules.naive_rule import NaiveRule
import pandas as Pd


if __name__ == '__main__':
    d = Pd.DataFrame({'x': [1, 2, 3]})
    m = Manager()
    m.add_rule(NaiveRule("rule 1", {'simple_list': d['x']}, param_max=2))
    m.execute()


