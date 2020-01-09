"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of Tower of Hanoi (recursive)


def hanoi(a, b, c, n):
    if n == 1:
        print("{} -> {}".format(a, c))
        return
    hanoi(a, c, b, n-1)  # rod a as source, rod b as target, rod c as pivot
    hanoi(a, b, c, 1)  # set the number of disk to be moved to 1
    hanoi(b, a, c, n-1)  # rod b as source, rod c as target, rod a as pivot


print("Solution of Tower of Hanoi with 4 disks: ", )
hanoi('a', 'b', 'c', 3)