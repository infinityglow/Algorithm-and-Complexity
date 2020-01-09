
"""
-*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# Euclid's algorithm to find the greatest common divisor with the complexity O(log n)

def gcd(m, n):
    while n != 0:
        r = m
        m = n
        n = r % n
        gcd(m, n)
    return m


m = 24; n = 16
print("The greatest common divisor of {} and {} is {}".format(m, n, gcd(m, n)))
