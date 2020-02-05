"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of polynomial computation followed by Horner's rule
# time complexity: Θ(n)

"""
# brute-force approach
# time complexity: Θ(n^2)
def poly_bf(coeffi_list, x):
    degree = len(coeffi_list) - 1  # highest degree
    result = 0
    for i in range(degree+1):
        coeffi = coeffi_list[i]; poly = 1
        for j in range(degree-i-1, -1, -1):
            poly *= x  # compute x^i
        result += coeffi * poly
    return result
"""

def poly_horner(coeffi_list, x):
    degree = len(coeffi_list) - 1  # highest degree
    result = coeffi_list[0]
    for i in range(1, degree+1):
        result = result * x + coeffi_list[i]
    return result


# compute the value of 2x^4 - 3x^3 + 5x^2 + x -7 at x = 4.
coefficient = [2, -3, 5, 1, -7]
x = 4
print(poly_horner(coefficient, x))  # should be 397

