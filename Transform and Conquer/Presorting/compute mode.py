"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of finding a mode in an array with the idea of presorting

"""
# brute-force approach
def compute_mode_bf(array):
    counter = {}
    for i in range(len(array)):
        counter[array[i]] = counter.get(array[i], 0) + 1
    freq = 0
    for key, value in counter.items():
        if value > freq:
            freq = value
            mode = key
    return mode
"""

def compute_mode_presort(array):
    array.sort()
    i = 0; freq = 0
    while i < len(array):
        temp_freq = 1; temp_mode = array[i]
        while i + temp_freq < len(array) and array[i+temp_freq] == temp_mode:
            temp_freq += 1
        if temp_freq > freq:
            freq = temp_freq; mode = temp_mode
        i += temp_freq
    return mode

array = [2, 6, 3, 1, 2, 1, 4, 2, 5, 3, 7, 8, 6, 4, 3]
print("The mode of the array is %d." % compute_mode_presort(array))