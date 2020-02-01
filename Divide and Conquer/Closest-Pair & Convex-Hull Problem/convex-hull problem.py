"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# solution of convex-hull problem (divide-and-conquer implementation)
# step:
# 1. find the leftmost and rightmost point p1 and pn
# 2. split scatter points into two parts, one of which is placed on the left side of vector p1pn,
#    while the other is on the right side
# 3. find a point pmax on both sides where the distance between p_max and vector p1pn is longest.
# 4. let p1p_max and p_maxpn be the new vector
# 5. find the new p_max on the left(right) side of vector in the upper(lower) hull.
# 6. execute step 3-5 recursively until there are no points left.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(13)

def compute_area(x1, y1, x2, y2, x3, y3):
    """
            | x1 y1 1 |
            | x2 y2 1 |
            | x3 y3 1 |
            compute determinant of the matrix above to obtain the area of a triangle
            if positive (x3, y3) is placed on the left side of vector q1q2,
            otherwise, on the right side
    """
    area = x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3
    return area
def compute_cos(x1, y1, x2, y2, x3, y3):
    # law of cosine to calculate angle
    a = np.sqrt((y3 - y2)**2 + (x3 - x2)**2)
    b = np.sqrt((y3 - y1)**2 + (x3 - x1)**2)
    c = np.sqrt((y2 - y1)**2 + (x2 - x1)**2)
    return -(b**2 + c**2 - a**2) / (2 * b * c)
def find_p_max(subset, p_left, p_right):
    # find point p_max which has the farthest from the line p1pn
    x1 = p_left[0]; y1 = p_left[1]
    x2 = p_right[0]; y2 = p_right[1]
    max_area = 0
    for i in range(len(subset)):
        x3 = subset[i][0]; y3 = subset[i][1]
        area = compute_area(x1, y1, x2, y2, x3, y3)
        if area > max_area:
            max_area = area
            angle = compute_cos(x1, y1, x2, y2, x3, y3)
            idx = i
        elif area == max_area:
            # if the area is the same, choose the point that maximizes angle ∠pmaxppn
            cur_angle = compute_cos(x1, y1, x2, y2, x3, y3)
            if cur_angle > angle:
                angle = cur_angle
                idx = i
    return subset[idx]
def is_in_set(p, p_left, p_right):
    # eliminate p and pn
    if p[0] == p_left[0] and p[1] == p_left[1] or p[0] == p_right[0] and p[1] == p_right[1]:
        return False
    return True
def generate_subset(totalset, p_left, p_right):
    # return subset of upper and lower points
    subset = np.array([[]])
    x1 = p_left[0]; y1 = p_left[1]
    x2 = p_right[0]; y2 = p_right[1]
    for i in range(len(totalset)):
        x3 = totalset[i][0]; y3 = totalset[i][1]
        area = compute_area(x1, y1, x2, y2, x3, y3)
        if area > 0 and is_in_set(totalset[i], p_left, p_right):
            if subset.shape[1] == 0:
                subset = np.append(subset, totalset[i][np.newaxis, :], axis=1)
            else:
                subset = np.append(subset, totalset[i][np.newaxis, :], axis=0)
    return subset
def quick_hull(subset, p_left, p_right):
    # return, if no points in the subset
    if subset.shape[1] == 0:
        return
    p_max = find_p_max(subset, p_left, p_right)
    global pairs
    pairs = np.append(pairs, p_max[np.newaxis, :], axis=0)
    upper_subset = generate_subset(subset, p_left, p_max)
    lower_subset = generate_subset(subset, p_max, p_right)
    quick_hull(upper_subset, p_left, p_max)
    quick_hull(lower_subset, p_max, p_right)
# for plotting
def plotting(hull_points, scatter_points):
    upper_points = np.array(generate_subset(hull_points, hull_points[0], hull_points[1]))
    lower_points = np.array(generate_subset(hull_points, hull_points[1], hull_points[0]))
    x_upper = sorted(upper_points[:, 0])
    x_lower = sorted(lower_points[:, 0], reverse=True)
    x = [hull_points[0][0]]; x.extend(x_upper); x.append(hull_points[1][0]); x.extend(x_lower); x.append(hull_points[0][0])
    y = []
    for key in x:
        y.append(XY_pair[key])
    plt.scatter(scatter_points[:, 0], scatter_points[:, 1], s=15)
    plt.plot(x, y, c='r')
    plt.grid()
    plt.show()

X = np.random.normal(2, 0.5, size=[16, 1])
Y = np.random.normal(2, 0.5, size=[16, 1])
XY = np.column_stack((X, Y))
pairs = np.array([[]])
XY_pair = {}

for i in range(len(X)):
    XY_pair[X.flatten()[i]] = Y.flatten()[i]
x = sorted(X.flatten())
p_left = np.array([[x[0], XY_pair[x[0]]]])
p_right = np.array([[x[-1], XY_pair[x[-1]]]])

pairs = np.append(pairs, p_left, axis=1)
pairs = np.append(pairs, p_right, axis=0)

upper_subset = np.array(generate_subset(XY, p_left[0], p_right[0]))
lower_subset = np.array(generate_subset(XY, p_right[0], p_left[0]))

quick_hull(upper_subset, p_left[0], p_right[0])
quick_hull(lower_subset, p_right[0], p_left[0])
plotting(pairs, XY)