# coding: utf-8
import pandas as pd
import numpy as np
from numpy.random import seed
from numpy.random import rand
from numpy.random import random_integers

seed(42)
N = 7

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
print "DataFrame\n", df
print pd.pivot_table(df, columns=["Food"], aggfunc=np.sum)
