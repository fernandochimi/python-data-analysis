# coding: utf-8
import scipy.misc
import matplotlib.pyplot as plt


ascent = scipy.misc.ascent()
acopy = ascent.copy()
aview = ascent.view()

plt.subplot(221)
plt.imshow(ascent)
plt.subplot(222)
plt.imshow(acopy)
plt.subplot(223)
plt.imshow(aview)
aview.flat = 0
plt.subplot(224)
plt.imshow(aview)
plt.show()
