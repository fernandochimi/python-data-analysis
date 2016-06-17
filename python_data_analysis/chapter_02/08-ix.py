# coding: utf-8
import scipy.misc
import matplotlib.pyplot as plt
import numpy as np


ascent = scipy.misc.ascent()
xmax = ascent.shape[0]
ymax = ascent.shape[1]


def shuffle_indices(size):
    arr = np.arange(size)
    np.random.shuffle(arr)
    return arr


xindices = shuffle_indices(xmax)
np.testing.assert_equal(len(xindices), xmax)
yindices = shuffle_indices(ymax)
np.testing.assert_equal(len(yindices), ymax)
plt.imshow(ascent[np.ix_(xindices, yindices)])
plt.show()
