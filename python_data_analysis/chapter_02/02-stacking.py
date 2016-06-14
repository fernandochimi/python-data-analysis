# coding: utf-8
import numpy as np


print "In: a"
a = np.arange(9).reshape(3, 3)
print a

print "In: b = 2 * a"
b = 2 * a
print b

print "In: hstack((a, b))"
hs = np.hstack((a, b))
print hs

print "In: concatenate((a, b), axis=1)"
cn = np.concatenate((a, b), axis=1)
print cn

print "In: vstack((a, b))"
vs = np.vstack((a, b))
print vs

print "In: concatenate((a, b), axis=1)"
cn = np.concatenate((a, b), axis=0)
print cn

print "In: dstack((a, b))"
ds = np.dstack((a, b))
print ds

print "In: oned = arange(2)"
oned = np.arange(2)
print oned
print "In: twice_oned = 2 * oned"
twice_oned = 2 * oned
print twice_oned
print "In: column_stack((oned, twice_oned))"
cs = np.column_stack((oned, twice_oned))
print cs

print "In: column_stack((a, b))"
cs_1 = np.column_stack((a, b))
print cs_1
print "In: column_stack((a, b)) == np.hstack((a, b))"
cs_2 = np.column_stack((a, b)) == np.hstack((a, b))
print cs_2

print "In: row_stack((oned, twice_oned))"
rs = np.row_stack((oned, twice_oned))
print rs

print "In: row_stack((a, b))"
rs_1 = np.row_stack((a, b))
print rs_1
print "In: row_stack((a, b)) == np.vstack((a, b))"
rs_2 = np.row_stack((a, b)) == np.vstack((a, b))
print rs_2
