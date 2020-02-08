"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

import random
import time

# implementation of heap sort
# to sort a random array with 10,000 elements
# two metrics ("number of comparison" and "consumed time") for efficiency evaluation
# time complexity: Θ(nlog n) in all cases
# space complexity: Θ(1)
# stability: unstable

random.seed(1)  # for reproducibility

def heaplify(array, temp_idx, size):
    cnt = 0
    temp_val = array[temp_idx]  # store value temporarily
    heap = False
    while not heap and 2 * temp_idx + 1 < size:
        j = 2 * temp_idx + 1  # index of left child
        # right child exists
        if j < size - 1:
            # compare two children
            if array[j] < array[j+1]:
                j = j + 1
        cnt += 1
        # whether violate heap property or not
        if array[j] <= temp_val:
            heap = True
        else:
            array[temp_idx] = array[j]
            temp_idx = j  # update temp_idx
        cnt += 1
    array[temp_idx] = temp_val
    return cnt

def heap_sort(array):
    cnt = 0
    for i in range((len(array)-2)//2, -1, -1):
        cnt += heaplify(array, i, len(array))
    for i in range(len(array)-1, -1, -1):
        array[0], array[i] = array[i], array[0]  # swap the first element with the last one
        cnt += heaplify(array, 0, i)
    return cnt


time_in_total = 0
epoch = 5  # num of iteration
total_comparison = 0

for i in range(epoch):
    time_start = time.time()
    array = [random.randint(0,10000) for i in range(10000)]
    comparison = heap_sort(array)
    time_finish = time.time()
    total_comparison += comparison
    time_in_total += time_finish - time_start
    print("Epoch {}: \n  number of comparison: {}\n  time consumed: {:.4f} s".format(i+1, comparison, time_finish-time_start))
print("average number of comparison: %d" % (total_comparison/epoch))
print('average time consumed: {:.4f} s'.format(time_in_total/epoch))

