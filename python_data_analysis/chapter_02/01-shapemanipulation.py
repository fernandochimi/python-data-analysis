# coding: utf-8
import numpy as np


print "In: b = arange(24).reshape(2, 3, 4)"
b = np.arange(24).reshape(2, 3, 4)
print "In: b"
print b

print "In: b.ravel()"
print b.ravel()

print "In: b.flatten()"
print b.flatten()

print "In: b.shape = (6, 4)"
b.shape = (6, 4)

print "In: b"
print b

print "In: b.transpose()"
print b.transpose()

print "In: b.resize((2, 12))"
b.resize((2, 12))

print "In: b"
print b
