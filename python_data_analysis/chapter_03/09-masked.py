# coding: utf-8
import numpy
import scipy
import matplotlib.pyplot as plt


ascent = scipy.misc.ascent()
random_mask = numpy.random.randint(0, 2, size=ascent.shape)

plt.subplot(221)
plt.title("Original")
plt.imshow(ascent)
plt.axis("off")

masked_array = numpy.ma.array(ascent, mask=random_mask)
print masked_array

plt.subplot(222)
plt.title("Masked")
plt.imshow(masked_array)
plt.axis("off")

plt.subplot(223)
plt.title("Log")
plt.imshow(numpy.log(ascent))
plt.axis("off")

plt.subplot(224)
plt.title("Log Masked")
plt.imshow(numpy.log(masked_array))
plt.axis("off")

plt.show()
