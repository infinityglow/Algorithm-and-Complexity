"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of quick sort
# to sort a random array with 10,000 elements
# two metrics ("number of comparison" and "consumed time") for efficiency evaluation
# time complexity: Θ(nlog n) for the best and average case and Θ(n^2) for the worst case
# space complexity Θ(1)
# stability: unstable

import time
import random
import sys
from array import generator

sys.setrecursionlimit(10010)  # set maximum recursion depth to 10000+

def partition(a):
    l = 0; r = len(a) - 1
    pivot = a[l]
    s = l
    global comparison
    for i in range(l+1, r+1):
        if a[i] < pivot:
            s += 1
            a[s], a[i] = a[i], a[s]
        comparison += 1
    a[l], a[s] = a[s], a[l]
    return s

def quick_sort(array):
    if len(array) > 1:
        s = partition(array)
        array[0: s] = quick_sort(array[0: s])
        array[s+1: len(array)] = quick_sort(array[s+1: len(array)])
    return array

time_in_total = 0
epoch = 5  # num of iteration
total_comparison = 0

# instantiate a generator
gen = generator(10000, 1)

# average case Θ(nlog n)
print("Average Case: ")
for i in range(epoch):
    array = gen.avg()
    time_start = time.time()
    comparison = 0
    quick_sort(array)
    time_finish = time.time()
    total_comparison += comparison
    time_in_total += time_finish-time_start
    print("Epoch {}: \n  number of comparison: {}\n  time consumed: {:.4f} s".format(i+1, comparison, time_finish-time_start))
print("average number of comparison: %d" % (total_comparison/epoch))
print('average time consumed: {:.4f} s'.format(time_in_total/epoch))

# worst case Θ(n^2)
print("Worst Case: ")
for i in range(epoch):
    array = gen.worst()
    time_start = time.time()
    comparison = 0
    quick_sort(array)
    time_finish = time.time()
    total_comparison += comparison
    time_in_total += time_finish-time_start
    print("Epoch {}: \n  number of comparison: {}\n  time consumed: {:.4f} s".format(i+1, comparison, time_finish-time_start))
print("average number of comparison: %d" % (total_comparison/epoch))
print('average time consumed: {:.4f} s'.format(time_in_total/epoch))
