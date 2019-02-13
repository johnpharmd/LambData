# a short file w 2 functions to be used for a LSDS project
# created 2019-02-13

import numpy as np
import pandas as pd


class UtilFuncs():
    def __init__(self, df):
        self.df = df

    def pprint_df_nulls(self):
    """
    Receives df parameter, then nicely prints out df columns with
    respective null counts
    """
        df1 = self.df.copy()
        df_nulls_dict = dict(df1.isna().sum())
        for col, null_count in df_nulls_dict.items():
            print(f'{col}: {null_count}')



