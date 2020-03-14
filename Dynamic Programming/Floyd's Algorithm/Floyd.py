"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of Floyd's algorithm
# this algorithm is for solving all-pairs shortest-paths problem
# starting from a distance matrix `d`, where infinity represents there is no direct path from one vertex to another
# and real number stands for distance between two vertices,
# the nested `for` loop compares the distance
# from ith vertex to jth vertex with the intermediate vertices numbered not higher than k-1
# and the distance from vertex i to vertex j with the intermediate vertices numbered not higher than k
# specifically, min(d[i][j], d[i][k]+d[k][j])
# then choose the smaller one as the entry of ith row, jth column
# after iteration, the distance matrix shows all-pairs shortest path
# time complexity: Θ(n^3), space complexity: Θ(n^2)

import numpy as np
from math import inf

def Floyd(d):
    n = d.shape[0]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
        print("After %d iteration:\n" % (k+1), d)
    return d


matrix = np.array([[0, 7, inf, inf, 1, 6],
                   [7, 0, 2, 4, inf, inf],
                   [inf, 2, 0, 9, 3, inf],
                   [inf, 4, 9, 0, inf, inf],
                   [1, inf, 3, inf, 0, 3],
                   [6, inf, inf, inf, 3, 0]])

print("Original matrix:\n", matrix)
d_matrix = Floyd(matrix)

# testing
bundle = [[1, 4], [3, 6], [5, 2]]
for i, (start, end) in enumerate(bundle):
    print("Test %d" % (i+1))
    print("The shortest distance between vertex {} and vertex {} is {}".
          format(start, end, int(d_matrix[start-1][end-1])))
