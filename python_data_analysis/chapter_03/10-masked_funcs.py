# coding: utf-8
import sys
from datetime import date

import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.finance import quotes_historical_yahoo


salary = np.loadtxt(
    "/home/fernando/Projects/python-data-analysis/" +
    "python_data_analysis/chapter_03/MLB2008.csv",
    delimiter=',', usecols=(1,), skiprows=1, unpack=True
)
triples = np.arange(0, len(salary), 3)
print "Triples", triples[:10], "..."

signs = np.ones(len(salary))
print "Signs", signs[:10], "..."

signs[triples] = -1
print "Signs", signs[:10], "..."

ma_log = np.ma.log(salary * signs)
print "Masked logs", ma_log[:10], "..."

dev = salary.std()
avg = salary.mean()
inside = np.ma.masked_outside(salary, avg - dev, avg + dev)
print "Inside", inside[:10], "..."

plt.subplot(311)
plt.title("Original")
plt.plot(salary)

plt.subplot(312)
plt.title("Log Masked")
plt.plot(np.exp(ma_log))

plt.subplot(313)
plt.title("Not extreme")
plt.plot(inside)

plt.show()
