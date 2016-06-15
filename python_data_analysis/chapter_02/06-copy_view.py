# coding: utf-8
import scipy.misc
import matplotlib.pyplot as plt


face = scipy.misc.face()
acopy = face.copy()
aview = face.view()

plt.subplot(221)
plt.imshow(face)
plt.subplot(222)
plt.imshow(acopy)
plt.subplot(223)
plt.imshow(aview)
aview.flat = 0
plt.subplot(224)
plt.imshow(aview)
plt.show()
