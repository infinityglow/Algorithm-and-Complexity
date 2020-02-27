"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# knapsack problem solved by dynamic programming(bottom-up)
# a two-dimensional array `table` initialized to 0 is created for storing temporary optima: table[i][j],
# which is subject to the constraint that 1<=i<=n, 1<=j<=W, where n = |weights|, and padded with 0 for i, j = 0
# entry in the table is calculated by the formula:
# table[i][j] = max(table[i-1][j], table[i-1][j-wi]+vi)  if j < wi
# table[i][j] = table[i-1][j]                            if j >= wi
# bottom-up method will calculate each entry in the table, i from 1 to n, j from 1 to W
# then the entry in the |weights|th row and Wth column is returned as the final solution
# optimal combination is found by backtracking
# in particular, if table[i][j] > table[i-1][j], then the ith item will be as the part of combination
# time complexity: Θ(nW); space complexity: Θ(nW)

import numpy as np

def backtracking(table, weights):
    i = len(table)-1; j = len(table[0])-1
    items = []
    while table[i][j] != 0:
        if table[i][j] > table[i-1][j]:
            items.append(i)
            j = j - weights[i-1]
        i = i - 1
    items.reverse()
    return items

def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)  # number of items
    table = np.zeros([n+1, capacity+1], dtype=np.int)
    print("Before iteration:\n", table)
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            wi = weights[i-1]; vi = values[i-1]
            if j < wi:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], table[i-1][j-wi] + vi)
    print("After iteration:\n", table)
    return table[n][capacity], table

weights = [7, 3, 4, 5]
values = [42, 12, 40, 25]
W = 10

print("Knapsack problem solved by dynamic programming(bottom-up):")
max_value, table = knapsack_bottom_up(weights, values, W)
combination = backtracking(table, weights)
print("The optimal combination is: ")
for i in range(len(combination)-1):
    print("item %d" % combination[i], end=', ')
print("item %d." % combination[-1])
print("The total value is %d." % max_value)