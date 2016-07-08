# coding: utf-8
import pandas as pd
import numpy as np


df = pd.read_csv(
    "/home/fernando/Projects/python-data-analysis/" +
    "python_data_analysis/chapter_04/WHO_first9cols.csv")
df = df[['Country', df.columns[-2]]][:2]
print "New df\n", df

print "Null values\n", pd.isnull(df)
print "Total Null Values\n", pd.isnull(df).sum()
print "Not Null Values\n", pd.notnull(df)
print "Last Column Doubled\n", 2 * df[df.columns[-1]]
print "Last Column Plus NaN\n", df[df.columns[-1]] + np.nan
print "Zero filled\n", df.fillna(0)
