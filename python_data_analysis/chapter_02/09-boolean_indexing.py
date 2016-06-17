# coding: utf-8
import scipy.misc
import matplotlib.pyplot as plt
import numpy as np


ascent = scipy.misc.ascent()


def get_indices(size):
    arr = np.arange(size)
    return arr % 4 == 0


ascent1 = ascent.copy()
xindices = get_indices(ascent.shape[0])
yindices = get_indices(ascent.shape[1])
ascent1[xindices, yindices] = 0
plt.subplot(211)
plt.imshow(ascent1)
ascent2 = ascent.copy()
ascent2[(ascent > ascent.max() / 4) & (ascent < 3 * ascent.max() / 4)] = 0
plt.subplot(212)
plt.imshow(ascent2)
plt.show()
