"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of checking element uniqueness with the idea of presorting
# time complexity: Θ(nlog n) + Θ(n) = Θ(nlog n)
# space complexity: Θ(1)

"""
# brute-force approach
# time complexity: Θ(n^2)
# space complexity: Θ(1)
def is_unique_bf(array):
    length = len(array)
    for i in range(length-1):
        element = array[i]
        for j in range(i+1, length):
            if array[j] == element:
                return False
    return True
"""

def is_unique_presort(array):
    length = len(array)
    array.sort()  # sort array
    for i in range(length-1):
        if array[i] == array[i+1]:
            return False
    return True


array = [3, 1, 6, 2, 7, 9]
# array = [2, 4, 1, 6, 2, 5]
if is_unique_presort(array):
    print("Elements in the array is unique.")
else:
    print("Elements in the array is not unique.")