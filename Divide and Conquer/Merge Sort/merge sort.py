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

def merge(A, B):
    i, j, k = 0, 0, 0  # initialize variables
    p, q = len(A), len(B)
    global comparison  # global variable
    C = [0 for i in range(p+q)]
    while i < p and j < q:
        if A[i] <= B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1
        comparison += 1
    while i < p:
        C[k] = A[i]
        i += 1; k += 1
    while j < q:
        C[k] = B[j]
        j += 1; k += 1
    return C

def merge_sort(array):
    if len(array) <= 1:
        return array
    m = len(array) // 2
    a = merge_sort(array[: m])
    b = merge_sort(array[m:])
    c = merge(a, b)
    return c

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

