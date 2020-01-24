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
        x = l + formula(l, r, key, array)
        if array[x] == key:
            return x
        elif array[x] < key:
            l = x + 1
        else:
            r = x - 1
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