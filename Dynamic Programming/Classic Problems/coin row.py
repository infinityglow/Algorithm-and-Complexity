"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# coin-row problem solved by dynamic programming
# suppose there is a row of n coins, whose values are d1, d2, ..., dm
# the goal is to pick up a combination that maximize the amount of money,
# subject to the constraint that two adjacent coins cannot be picked up concurrently
# an array `optima` with length n is created to temporary optimal value
# each entry in `optima` is calculated by the formula: F(i) = max(F(i-1), F(i-2)+Ci)
# where Ci represents the ith coin in a row of n coins
# optimal combination is found by backtracking
# in particular, if F(i) > F(i-1), then the ith coin will be as the part of combination
# time complexity: Θ(n); space complexity: Θ(n)

def coin_row_bf(coins, n):
    if n == 0:
        return 0
    if n == 1:
        return coins[n-1]  # ignore adjacent coin
    return max(coin_row_bf(coins, n-2), coin_row_bf(coins, n-1) + coins[n-1])

def coin_row_dp(coins, n):
    optima = [-1 for i in range(n+1)]
    optima[0] = 0; optima[1] = coins[0]
    global combination
    for i in range(2, n+1):
        # max(F(n-2), F(n-1)+Cn)
        if optima[i-1] < optima[i-2] + coins[i-1]:
            optima[i] = optima[i-2] + coins[i-1]
        else:
            optima[i] = optima[i-1]
    # backtracking
    while n > 0:
        if optima[n] > optima[n-1]:
            combination[n-1] = 1
            n -= 2
        else:
            n -= 1
    return optima[-1]


coins = [10, 20, 50, 20, 5, 20, 10, 50]
# 1 means the coin in the position will be picked up, while 0 does not
# e.g. [1, 0, 1, 0, 1, 0, 1] means the 1st, 3rd, 5th and 7th coin are selected
combination = [0 for i in range(len(coins))]
print("Coin-row problem solved by dynamic programming:")
print("Coin arrangement: \n", coins)
print("The maximum amount of money is %d." % coin_row_dp(coins, len(coins)))
print("The choice for each coin:\n", combination)