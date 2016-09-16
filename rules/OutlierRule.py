from rules.rule_base import BaseRule
import pandas as pd


class OutlierRule(BaseRule):
    def __init__(self, name, mapping, range=0.1, direction='upper'):
        self.name = name
        # rule specific attributes
        self.df = None
        self.dim = None
        self.idvar = None
        self.valuevar = None
        self.range = range
        self.direction = direction
        self.args = ['df', 'dim', 'idvar', 'valuevar']
        self.bind(mapping)

    # TODO validate rule args
    def execute(self):
        for arg in self.args:
            if not hasattr(self, arg):
                raise AttributeError("%arg not specified, please run `bind` first " % arg)
        result = {}
        for d in self.dim:
            benchmark = self.df.groupby([d]).mean()[self.valuevar].reset_index()
            benchmark.columns = [x+"_y" for x in benchmark.columns]
            df_rank = pd.merge(self.df, benchmark, left_on=d, right_on=d+"_y")
            if self.direction == "upper":
                outlier_ids = df_rank[df_rank[self.valuevar]>df_rank[self.valuevar+"_y"]*(1+self.range)][self.idvar].unique()
                if len(outlier_ids):
                    result[d] = outlier_ids
        return result
