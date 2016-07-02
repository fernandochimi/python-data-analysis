# coding: utf-8
from pandas.io.parsers import read_csv


df = read_csv(
    "/home/fernando/Projects/python-data-analysis/" +
    "python_data_analysis/chapter_04/WHO_first9cols.csv")
print "DataFrame", df
print "Shape", df.shape
print "Length", len(df)
print "Column Headers", df.columns
print "Data types", df.dtypes
print "Index", df.index
print "Values", df.values
