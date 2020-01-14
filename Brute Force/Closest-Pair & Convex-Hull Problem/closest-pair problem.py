"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# solution of closest-pair problem (brute-force implementation)
# method: enumerate all pairs of points, compute their distance, and find the minimal value

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(13)  # for reproducibility

def closest_pair_bf(X, Y):
    d = np.inf  # initialize d to infinity
    for i in range(len(X)-1):
        for j in range(i+1, len(X)):
            if (X[i] - X[j])**2 + (Y[i] - Y[j])**2 < d:
                d = (X[i] - X[j])**2 + (Y[i] - Y[j])**2
                coordinates = np.array([[X[i][0], Y[i][0]], [X[j][0], Y[j][0]]])  # record coordinates of temporary pair
    d = np.sqrt(d)
    return d, coordinates

# for plotting
def plotting(xy_pair, d, pair):
    plt.scatter(xy_pair[:, 0], xy_pair[:, 1], s=15)
    plt.plot(pair[:, 0], pair[:, 1], c='r')
    plt.text(1.35, 3, "closest distance = %.3f" % d)
    plt.grid()
    plt.show()

X = np.random.normal(2, 0.5, size=[16, 1])
Y = np.random.normal(2, 0.5, size=[16, 1])
XY_pair = np.column_stack((X, Y))  # stack to (xi, yi)
min_d, clo_pair = closest_pair_bf(X, Y)

plotting(XY_pair, min_d, clo_pair)