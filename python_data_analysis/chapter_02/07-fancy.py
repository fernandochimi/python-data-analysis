# coding: utf-8
import scipy.misc
import matplotlib.pyplot as plt


face = scipy.misc.face()
xmax = face.shape[0]
ymax = face.shape[1]
face[range(xmax), range(ymax)] = 0
face[range(xmax - 1, -1, -1), range(ymax)] = 0
plt.imshow(face)
plt.show()
