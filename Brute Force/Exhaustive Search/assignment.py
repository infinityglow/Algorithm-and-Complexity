"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of assignment problem solved by brute-force approach

import numpy as np

def perm_gen(source):
    permutation = [[source[0]]]
    for i in range(1, len(source)):
        temp = []  # rewrite for each iteration
        for p in permutation:
            for j in range(len(p), -1, -1):
                p.insert(j, source[i])
                temp.append(p.copy())
                p.pop(j)
        permutation = temp.copy()
    return permutation

def assignment_bf(perm, table):
    combination = None; min_cost = np.inf
    for i in range(len(perm)):
        temp_cost = 0  # accumulator
        for j, k in enumerate(perm[i]):
            temp_cost += table[j][k-1]
        if temp_cost < min_cost:
            combination = perm[i]
            min_cost = temp_cost
    return combination, min_cost


table = np.array([[9, 2, 7, 8],
                       [6, 4, 3, 7],
                       [5, 8, 1, 8],
                       [7, 6, 9, 4]])

num_staff = len(table)
permutation = perm_gen(list(range(1, num_staff+1)))
combination, min_cost = (assignment_bf(permutation, table))

print("The optimal assignment is")
for i in range(num_staff-1):
    print("assign task {} to staff {}".format(combination[i], i+1), end=', ')
print("task {} to staff {}.".format(combination[-1], num_staff))
print("The minimal cost is %d." % min_cost)



