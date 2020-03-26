"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of 8-queen problem solved by backtracking technique
# starting from an empty chessboard, we place the first queen in the
# row 1 column 1, then we attempt to place the second queen in each column in row 2
# if two queens do not attack each other, we place the third queen, and so on
# if either two queens attack each other(dead end), we backtrack and check the next possible option
# loop over the previous steps until a solution is generated
# time complexity: depends on the problem instance, can be exponential or factorial in the worst case


def is_promising(table, row):
    # whether it is the same column
    if len(set(table[: row+1])) != len(table[: row+1]):
        return False
    # whether it is the same diagonal
    for i in range(row):
        if abs(table[row] - table[i]) == row - i:
            return False
    return True
def display_board(table):
    n = len(table)
    for col in table:
        print("+ " * (col) + "Q " + "+ " * (n-1-col))
def display(table, cnt):
    if cnt:
        print("Solution %d:" % cnt)
        display_board(table)
    else:
        print("Solution: ")
        display_board(table)

def backtracking(table, n, is_mul, row=0):
    if row == n:  # initial condition
        if is_mul:
            global cnt  # counter for multiple solutions
            display(table, cnt+1); cnt += 1
        else:
            display(table, None)
            exit()  # terminate program
        return
    for col in range(n):
        table[row] = col
        if is_promising(table, row):
            backtracking(table, n, is_mul, row+1)  # search the next level
def queen(n, multiple=False):
    """
    :param n: size of chessboard
    :param multiple: is print multiple solutions
    """
    col_tab = [-1] * n
    backtracking(col_tab, n, is_mul=multiple)


cnt = 0  # a global variable to count the solution
# you can set your own chessboard size and pass the second param `True` to print the entire solution set
queen(8)

"""
Q + + + + + + + 
+ + + + Q + + + 
+ + + + + + + Q 
+ + + + + Q + + 
+ + Q + + + + + 
+ + + + + + Q + 
+ Q + + + + + + 
+ + + Q + + + +
"""
