# coding: utf-8
import pandas as pd
import numpy as np
from numpy.random import seed
from numpy.random import rand
from numpy.random import random_integers

seed(42)


df = pd.DataFrame(
    {
        "Weather": [
            "cold", "hot", "cold", "hot",
            "cold", "hot", "cold"
        ],
        "Food": [
            "soup", "soup", "icecream", "chocolate",
            "icecream", "icecream", "soup"
        ],
        "Price": 10 * rand(7),
        "Number": random_integers(1, 9, size=(7, ))
    })
print df

weather_group = df.groupby("Weather")

i = 0

for name, group in weather_group:
    i += 1
    print "Group", i, name
    print group

print "Weather group first\n", weather_group.first()
print "Weather group last\n", weather_group.last()
print "Weather group mean\n", weather_group.mean()

wf_group = df.groupby(["Weather", "Food"])
print "WF Groups", wf_group.groups

print "WF Aggregated\n", wf_group.agg([np.mean, np.median])

print "df :3\n", df[:3]

print "Concat back together\n", pd.concat([df[:3], df[3:]])

print "Appending rows\n", df[:3].append(df[5:])
