"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of assignment problem solved by branch-and-bound technique
# starting from the initial state, for each column of the first row, we calculate
# the lower bound of the remaining rows. After comparing all states' lower bound,
# we choose the smallest one as the next state. Loop over the previous procedures,
# the solution is obtained from the last level of the state-space tree


import numpy as np

class State(object):
    def __init__(self, matrix, lb, row, process):
        self.matrix = matrix  # save the current state
        self.lb = lb  # lower bound for current state
        self.process = process  # processed values
        self.row = row  # current row
def compute_lower_bound(a):
    return np.sum(np.min(a, axis=1))
def fix_up(queue):
    temp_idx = len(queue) - 1
    parent_idx = (temp_idx - 1) // 2
    heap = False
    while not heap and parent_idx >= 0:
        # swap elements if heap property is violated
        if queue[temp_idx].lb < queue[parent_idx].lb:
            queue[temp_idx], queue[parent_idx] = queue[parent_idx], queue[temp_idx]
        else:
            heap = True
        # update indices
        temp_idx = parent_idx
        parent_idx = (temp_idx - 1) // 2
def fix_down(queue):
    if not queue:
        return
    temp_idx = 0; size = len(queue)
    temp_ver = queue[temp_idx]  # save vertex temporarily
    heap = False
    while not heap and 2 * temp_idx + 1 < size:
        j = 2 * temp_idx + 1  # index of left child
        # right child exists
        if j < size - 1:
            # compare two children's weight
            if queue[j].lb > queue[j + 1].lb:
                j = j + 1
        # whether violate heap property or not
        if queue[j].lb >= temp_ver.lb:
            heap = True
        else:
            queue[temp_idx] = queue[j]
            temp_idx = j  # update temp_idx
    queue[temp_idx] = temp_ver
def main(c):
    row, col = c.shape
    pqueue = []
    cur_state = State(c, 0, 0, 0)  # initial state
    pqueue.append(cur_state)
    while cur_state.row < row-1:
        cur_state = pqueue.pop()
        fix_down(pqueue)
        cur_matrix = cur_state.matrix; cur_row = cur_state.row
        for cur_col in range(col):
            if cur_matrix[cur_row][cur_col] != np.inf:
                temp_matrix = cur_matrix.copy()
                temp_matrix[cur_row, :] = np.inf; temp_matrix[:, cur_col] = np.inf
                lower_bound = compute_lower_bound(temp_matrix[cur_row+1:]) + cur_state.process + cur_matrix[cur_row][cur_col]
                process = cur_state.process + cur_matrix[cur_row][cur_col]
                pqueue.append(State(temp_matrix, lower_bound, cur_row+1, process))
                fix_up(pqueue)
        pqueue[0], pqueue[-1] = pqueue[-1], pqueue[0]
    return cur_state.lb

C = np.array([[9, 5, 7, 6],
              [6, 4, 3, 7],
              [5, 8, 1, 8],
              [4, 6, 9, 4]], dtype=np.float)
print("The minimal cost is %d." % main(C))