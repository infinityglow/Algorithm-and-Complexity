"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of counting sort
# to sort a random array with 10,000 elements
# two metrics ("number of comparison" and "consumed time") for efficiency evaluation
# time complexity: Θ(n+k) in all cases,
# where n is the number of elements in an array and k is the number of buckets for counting
# space complexity Θ(k)
# stability: unstable

import time
import random

def counting_sort(array):
    largest = max(array); smallest = min(array)  # get the largest and smallest value
    bucket = [0 for i in range(largest-smallest+1)]  # empty bucket array for counting
    idx = 0  # index for rearranging array
    cnt = 0
    for i in range(len(array)):
        bucket[array[i]-smallest] += 1
    for j in range(len(bucket)):
        while bucket[j] > 0:
            array[idx] = j + smallest
            idx += 1
            bucket[j] -= 1
    return cnt


time_in_total = 0
epoch = 5  # num of iteration
total_comparison = 0

for i in range(epoch):
    time_start = time.time()
    array = [random.randint(0,10000) for i in range(10000)]
    comparison = counting_sort(array)
    time_finish = time.time()
    total_comparison += comparison
    time_in_total += time_finish - time_start
    print("Epoch {}: \n  number of comparison: {}\n  time consumed: {:.4f} s".format(i+1, comparison, time_finish-time_start))
print("average number of comparison: %d" % (total_comparison/epoch))
print('average time consumed: {:.4f} s'.format(time_in_total/epoch))

