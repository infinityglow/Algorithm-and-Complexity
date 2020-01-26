"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of merge sort
# to sort a random array with 10,000 elements
# two metrics ("number of comparison" and "consumed time") for efficiency evaluation
# time complexity: Θ(nlog n) in all cases
# space complexity Θ(n)
# stability: stable

import time
import random

def merge(a, b):
    i, j, k = 0, 0, 0  # initialize variables
    p, q = len(a), len(b)
    global comparison  # global variable
    c = [0 for i in range(p+q)]
    while i < p and j < q:
        if a[i] <= b[j]:
            c[k] = a[i]; i += 1
        else:
            c[k] = b[j]; j += 1
        k += 1
        comparison += 1
    while i < p:
        c[k] = a[i]
        i += 1; k += 1
    while j < q:
        c[k] = b[j]
        j += 1; k += 1
    return c

def merge_sort(array):
    if len(array) <= 1:
        return array
    m = len(array) // 2  # middle position
    A = merge_sort(array[: m])
    B = merge_sort(array[m:])
    C = merge(A, B)
    return C

time_in_total = 0
epoch = 5  # num of iteration
total_comparison = 0

for i in range(epoch):
    time_start = time.time()
    array = [random.randint(0,10000) for i in range(10000)]
    comparison = 0
    merge_sort(array)
    time_finish = time.time()
    total_comparison += comparison
    time_in_total += time_finish - time_start
    print("Epoch {}: \n  number of comparison: {}\n  time consumed: {:.4f} s".format(i+1, comparison, time_finish-time_start))
print("average number of comparison: %d" % (total_comparison/epoch))
print('average time consumed: {:.4f} s'.format(time_in_total/epoch))

