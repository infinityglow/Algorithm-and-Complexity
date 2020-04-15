"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of matrix multiplication (2 × 2 square matrix)
# time complexity: Θ(n^3)


def matmul(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C


A = [[-3, 1], [2, 5]]
B = [[5, 3], [7, -3]]
print("A = \n", A)
print("B = \n", B)
print("AB = \n", matmul(A, B))
