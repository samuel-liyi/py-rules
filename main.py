from manager.manager import Manager
from rules.naive_rule import NaiveRule
import pandas as Pd


if __name__ == '__main__':
    d = Pd.DataFrame({'x': [1, 2, 3]})
    m = Manager(d)
    m.add_rule(NaiveRule("rule 1", {'max_v': 2}), {'x': 'x'})
    m.add_rule(NaiveRule("rule 2", {'max_v': 4}), {'x': 'x'})
    m.execute()


