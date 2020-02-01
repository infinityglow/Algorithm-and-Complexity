"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# solution of closest-pair problem (divide-and-conquer implementation)
# step:
# 1. split scatter points into two parts
# 2. calculate the closest pairs of left and right parts respectively
# 3. choose the shorter one d
# 4. let m equals to the middle point
# 5. copy all points for which |x - m| < d into array S
# 6. if the region x±d exists a pair such that the distance between them is shorter than d,
#     let the pair be the closest pair and update d
# 7. do this operation recursively until the number of points is less than or equal to three,
#     then the brute-force approach is used to find the closest pair.

import numpy as np
import matplotlib.pyplot as plt

def brute_force(x, y):
    dmin = np.inf  # initialize dmin to infinity
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 < dmin:
                dmin = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
                coordinates = np.array([[x[i], y[i]], [x[j], y[j]]])
    return dmin, coordinates

def closest_pair_dc(P, Q, n):
    if n <= 3:
        return brute_force(P, Q)
    else:
        left = (len(P) + 1) // 2; right = len(P) - left  # number of points of left and right part
        P_left = P[:left]; P_right = P[left:]
        Q_left = Q[:left]; Q_right = Q[left:]
        d_left, pair_left = closest_pair_dc(P_left, Q_left, left)  # find the closest pair from the left recursively
        d_right, pair_right = closest_pair_dc(P_right, Q_right, right)  # find the closest pair from the right recursively
        # choose the shorter one
        if d_left < d_right:
            d = d_left; temp_pair = pair_left
        else:
            d = d_right; temp_pair = pair_right
        m = P[(len(P)) // 2]
        S = []  # points within the region |x - m| < d for temporary storage
        # copy
        for key in P:
            if abs(key - m) < d:
                S.append(key)
        for i in range(len(S) - 1):
            j = i + 1
            while j < len(S) and (XY_pair[S[i]] - XY_pair[S[j]]) ** 2 < d:
                if (S[i] - S[j]) ** 2 + (XY_pair[S[i]] - XY_pair[S[j]]) ** 2 < d:
                    d = (S[i] - S[j]) ** 2 + (XY_pair[S[i]] - XY_pair[S[j]]) ** 2  # update d
                    temp_pair = np.array([[S[i], XY_pair[S[i]]], [S[j], XY_pair[S[j]]]])  # update pair
                j += 1
    return d, temp_pair

# for plotting
def plotting(d, pair):
    plt.scatter(x, y, s=15)
    plt.text(1.35, 3, s="closest distance = %.3f" % d ** (1 / 2))
    plt.plot((pair[0][0], pair[1][0]), (pair[0][1], pair[1][1]), c='r')
    plt.grid()
    plt.show()

np.random.seed(13)  # for reproducibility
X = np.random.normal(2, 0.5, size=[16, 1])
Y = np.random.normal(2, 0.5, size=[16, 1])
XY_pair = {}

for i in range(len(X)):
    XY_pair[X.flatten()[i]] = Y.flatten()[i]

x = sorted(X.flatten())
y = []
for x_i in x:
    y.append(XY_pair[x_i])

dmin, pair = closest_pair_dc(x, y, len(XY_pair))
plotting(dmin, pair)