# coding: utf-8
import numpy as np


print "In: b"
b = np.arange(24).reshape(2, 12)
print b

print "In: b.ndim"
print b.ndim

print "In: b.size"
print b.size

print "In: b.itemsize"
print b.itemsize

print "In: b.nbytes"
print b.nbytes

print "In: b.size * b.itemsize"
print b.size * b.itemsize

print "In: b.resize(6, 4)"
print b.resize(6, 4)

print "In: b"
print b

print "In: b.T"
print b.T

print "In: b.ndim"
print b.ndim

print "In: b.T"
print b.T

print "In: b = array([1.j + 1, 2.j + 3])"
b = np.array([1.j + 1, 2.j + 3])

print "In: b"
print b

print "In: b.real"
print b.real

print "In: b.imag"
print b.imag

print "In: b.dtype"
print b.dtype

print "In: b.dtype.str"
print b.dtype.str

print "In: b = arange(4).reshape(2, 2)"
b = np.arange(4).reshape(2, 2)
print "In: b"
print b

print "In: f = b.flat"
f = b.flat
print "In: f"
print f

print "In: for it in f: print it"
for it in f:
    print it

print "In: b.flat[2]"
print b.flat[2]

print "In: b.flat[[1, 3]]"
print b.flat[[1, 3]]

print "In: b"
print b

print "In: b.flat[[1, 3]] = 1"
b.flat[[1, 3]] = 1
print "In: b"
print b
