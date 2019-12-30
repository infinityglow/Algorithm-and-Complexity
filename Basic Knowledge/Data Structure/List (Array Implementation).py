"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

#  sequential list (array implementation) and its three operations: Search, Insert and Remove

def search(array, element):
    length = len(array)
    for i in range(length):
        if array[i] == element:
            return i
    return -1

def insert(array, idx, element):
    new_array = array.copy() + [None]  # copy elements into a new array
    length = len(new_array); i = length - 1
    # shift elements after idx i to the right by 1 position
    while i > idx:
        new_array[i] = new_array[i-1]
        i -= 1
    new_array[idx] = element
    return new_array

def remove(array, element):
    length = len(array)
    idx = search(array, element)  # find index
    if idx != -1:
        while idx < length - 1:
            array[idx] = array[idx+1]
            idx += 1
        array = array[: -1]
    return array


array = [24, 22, 76, 41, 7, 61, 15, 34, 80]
print("The original array: \n", array)
# search element 61
print("Search element 61: ")
if search(array, 61) != -1:
    print("Search is successful!")
else:
    print("Search is unsuccessful!")
# remove element 61
array = remove(array, 61)
print("After removing 61: \n", array)
# insert element 61
array = insert(array, 5, 61)
print("After inserting 61: \n", array)