# coding: utf-8
import numpy as np
import pandas as pd

np.random.seed(42)

a = np.random.randn(3, 4)
a[2][2] = np.nan
print a

np.savetxt(
    "/home/fernando/Projects/python-data-analysis/" +
    "python_data_analysis/chapter_05/np.csv", a,
    fmt="%.2f", delimiter=",", header=" #1, #2, #3, #4")

df = pd.DataFrame(a)
print df

df.to_csv(
    "/home/fernando/Projects/python-data-analysis/" +
    "python_data_analysis/chapter_05/pd.csv",
    float_format="%.2f", na_rep="NAN!")
