# coding: utf-8
import scipy.misc
import matplotlib.pyplot as plt


ascent = scipy.misc.ascent()
xmax = ascent.shape[0]
ymax = ascent.shape[1]
ascent[range(xmax), range(ymax)] = 0
ascent[range(xmax - 1, -1, -1), range(ymax)] = 0
plt.imshow(ascent)
plt.show()
