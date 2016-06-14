# coding: utf-8
import numpy as np


print "In: a"
a = np.arange(9).reshape(3, 3)
print a

print "In: b = 2 * a"
b = 2 * a
print b

print "In: hsplit(a, 3)"
hs = np.hsplit(a, 3)
print hs

print "In: split(a, 3, axis=1)"
s = np.split(a, 3, axis=1)
print s

print "In: vsplit(a, 3)"
vs = np.vsplit(a, 3)
print vs

print "In: split(a, 3, axis=0)"
s_1 = np.split(a, 3, axis=0)
print s_1

print "In: arange(27).reshape(3, 3, 3)"
c = np.arange(27).reshape(3, 3, 3)
print c

print "In: dsplit(c, 3)"
ds = np.dsplit(c, 3)
print ds
