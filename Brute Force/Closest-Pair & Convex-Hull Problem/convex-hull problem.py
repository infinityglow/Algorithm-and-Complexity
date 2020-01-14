"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# solution of convex-hull problem (brute-force implementation)
# step:
# 1. enumerate all pairs of points
# 2. for each pair, check the remaining points whether they stand in the same side
# 3. select those pair that all the remaining points
# time complexity: Θ(n^3)

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(13)  # for reproducibility

def convex_hull_bf(XY_pair):
    pairs = []
    for i in range(len(XY_pair) - 1):
        for j in range(i+1, len(XY_pair)):
            a = XY_pair[j][1] - XY_pair[i][1]
            b = XY_pair[i][0] - XY_pair[j][0]
            c = XY_pair[i][0] * XY_pair[j][1] - XY_pair[i][1] * XY_pair[j][0]
            k = 0; pos = 0; neg = 0  # pos and neg count the number of points on either side respectively
            while k < len(XY_pair):
                if k != i and k != j:
                    if a * XY_pair[k][0] + b * XY_pair[k][1] - c > 0:
                        pos += 1
                    else:
                        neg += 1
                    if pos != 0 and neg != 0:
                        break
                k += 1
            else:
                pairs.append((XY_pair[i], XY_pair[j]))
    return pairs

# for plotting
def plotting(xy_pair, polygon):
    plt.scatter(xy_pair[:, 0], xy_pair[:, 1], s=15)
    for i in range(len(polygon)):
        np_point_stack = np.stack(polygon[i], axis=1)  # stack each point pair to (xi, yi)
        plt.plot(np_point_stack[0], np_point_stack[1], c='r')
    plt.show()

X = np.random.normal(2, 0.5, size=[16, 1])
Y = np.random.normal(2, 0.5, size=[16, 1])
XY_pair = np.column_stack((X, Y))
polygon = convex_hull_bf(XY_pair)
plotting(XY_pair, polygon)
