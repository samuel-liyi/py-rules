from manager.manager import Manager
from rules.naive_rule import NaiveRule
from rules.outlier_rule import  outlier_rule
import pandas as Pd


if __name__ == '__main__':
    d = Pd.DataFrame({'x': [1, 2, 3]})
    d2 = Pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': ['a', 'a', 'a', 'c', 'c'], 'z' : ['j', 'q', 'x', 'w', 's']})
    m = Manager()
    m.add_rule(NaiveRule("rule 1", {'simple_list': d['x']}, param_max=2))
    m.add_rule(outlier_rule("rule 2", {"df": d2, "dim": ["y"], "idvar": 'z', 'valuevar': 'x'}))
    m.execute()


