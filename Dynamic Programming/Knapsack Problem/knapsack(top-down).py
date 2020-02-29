"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# knapsack problem solved by dynamic programming(top-down)
# we create a two-dimensional array `table` initialized to special symbol(-1)
# which is subject to the constraint that 1<=i<=n, 1<=j<=W, where n = |weights|, and padded with 0 for i, j = 0
# entry in the table is calculated by the formula:
# table[i][j] = max(table[i-1][j], table[i-1][j-wi]+vi)  if j < wi
# table[i][j] = table[i-1][j]                            if j >= wi
# top-down method only calculates part of entries
# whenever a new value needs to be calculated, the corresponding entry is checked
# if the entry is equal to -1, the recursion goes deeper until base case
# otherwise, the value in the entry is retrieved from the table
# the entry in the |weights|th row and Wth column is returned as the final solution
# optimal combination is found by backtracking
# in particular, if table[i][j] > table[i-1][j], then the ith item will be as the part of combination
# time complexity: Θ(nW); space complexity: Θ(nW)

import numpy as np

def backtracking(table, weights):
    i = len(table)-1; j = len(table[0])-1
    items = []
    while table[i][j] != -1 and table[i][j] != 0:
        if table[i][j] > table[i-1][j]:
            items.append(i)
            j = j - weights[i-1]
        i = i - 1
    items.reverse()
    return items

def knapsack_top_down(t, w, v, i, j):
    if t[i][j] < 0:
        if j < w[i-1]:
            t[i][j] = knapsack_top_down(t, w, v, i-1, j)
        else:
            t[i][j] = max(knapsack_top_down(t, w, v, i-1, j), knapsack_top_down(t, w, v, i-1, j-w[i-1])+v[i-1])
    return t[i][j]


def knapsack_top_down_main(weights, values, capacity):
    n = len(weights)
    table = np.zeros([n+1, capacity+1], dtype=np.int) - 1
    table[0, :] = 0; table[:, 0] = 0  # pad with 0 in the first row and column
    print("Before recursion:\n", table)
    maximum = knapsack_top_down(table, weights, values, n, capacity)
    print("After recursion:\n", table)
    return maximum, table


weights = [7, 3, 4, 5]
values = [42, 12, 40, 25]
W = 10

print("Knapsack problem solved by dynamic programming(top-down):")
max_value, table = knapsack_top_down_main(weights, values, W)
combination = backtracking(table, weights)
print("The optimal combination is: ")
for i in range(len(combination)-1):
    print("item %d" % combination[i], end=', ')
print("item %d." % combination[-1])
print("The total value is %d." % max_value)