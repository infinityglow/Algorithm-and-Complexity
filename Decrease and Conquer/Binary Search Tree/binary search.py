"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of binary search
# time complexity: Θ(log n)

def binary_search(array, key):
    l = 0; r = len(array) - 1
    while l <= r:
        m = (l + r) // 2  # 向下取整
        if key == array[m]:
            return m
        elif key < array[m]:
            r = m - 1
        else:
            l = m + 1
    return -1


array = [10, 25, 34, 48, 61, 73, 81]
key1 = 61; key2 = 76
print("Binary Search: ")

#
print("search key = %d" % key1)
if binary_search(array, key1) != -1:
    print("Search successful. The index is %d." % binary_search(array, key1))
else:
    print("Search unsuccessful.")

print("search key = %d" % key2)
if binary_search(array, key2) != -1:
    print("Search successful. The index is %d." % binary_search(array, key2))
else:
    print("Search unsuccessful.")