"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of interpolation search
# time complexity: Θ(log log n)

def formula(l, r, key, array):
    p = (key - array[l]) / (array[r] - array[l])
    n = r - l
    idx = int(n * p)
    return idx

def interpolation_search(array, key):
    l = 0; r = len(array) - 1
    while l <= r:
        m = l + formula(l, r, key, array)
        if array[m] == key:
            return m
        elif array[m] < key:
            l = m + 1
        else:
            r = m - 1
    return -1


array = [10, 25, 34, 48, 61, 73, 81]
key1 = 61; key2 = 67
print("Interpolation Search: ")

# success
print("search key = %d" % key1)
if interpolation_search(array, key1) != -1:
    print("Search successful. The index is %d." % interpolation_search(array, key1))
else:
    print("Search unsuccessful.")

# fail
print("search key = %d" % key2)
if interpolation_search(array, key2) != -1:
    print("Search successful. The index is %d." % interpolation_search(array, key2))
else:
    print("Search unsuccessful.")