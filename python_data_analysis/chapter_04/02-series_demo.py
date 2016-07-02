# coding: utf-8
import numpy as np
from pandas.io.parsers import read_csv


df = read_csv(
    "/home/fernando/Projects/python-data-analysis/" +
    "python_data_analysis/chapter_04/WHO_first9cols.csv")
country_col = df["Country"]
print "Type DataFrame", type(df)
print "Type country col", type(country_col)
print "Series shape", country_col.shape
print "Series index", country_col.index
print "Series values", country_col.values
print "Series name", country_col.name
print "Last 2 countries", country_col[-2:]
print "Last 2 countries type", type(country_col[-2:])
# print "df Signs", np.sign(df)
last_col = df.columns[-1]
print "Last df column signs", last_col, np.sign(df[last_col])
print np.sum(df[last_col] - df[last_col].values)
