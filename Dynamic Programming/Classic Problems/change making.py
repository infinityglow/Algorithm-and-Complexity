"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# change-making problem solved by dynamic programming
# given coins with the different denominations d1<d2<...<dm,
# and each denomination can be selected more than once
# the goal is to use the minimum number of coins to make up amount n
# `optima` array is created to store temporary optimal value
# each entry in `optima` is calculated by the formula: F(n) = {F(n-dj)} + 1 for each dj in {d}
# where dj represents the jth coin in coin set {d}
# optimal combination is found by backtracking
# in particular, if F(i) > F(i-dj) for each dj in {d},
# then the denomination dj will be as the part of combination
# time complexity: Θ(mn); space complexity: Θ(n)

from math import inf

def change_making_bf(money, amount):
    if amount == 0:
        return 0
    cnt = inf
    for m in money:
        if m <= amount:
            cnt = min(cnt, change_making_bf(money, amount-m) + 1)
    return cnt

def change_making_dp(money, amount):
    optima = [0 for i in range(amount+1)]
    global combination
    for i in range(1, amount+1):
        temp = inf
        j = 0
        # min({F(n-di)|1<=i<=m}) if n-di > 0
        while j < len(money) and i >= money[j]:
            temp = min(temp, optima[i-money[j]])
            j += 1
        optima[i] = temp + 1
    # backtracking
    while amount > 0:
        temp = inf; idx = 0
        for k in range(len(money)):
            if amount-money[k] < 0:
                break
            if optima[amount-money[k]] < temp:
                temp = optima[amount-money[k]]
                idx = k
        combination.append(money[idx])
        amount -= money[idx]
    return optima[-1]


denomination = [1, 5, 10, 20, 50, 100]
amount = 396
combination = []
print("Change-making problem solved by dynamic programming: ")
print("Denominations:\n", denomination)
print("The minimum number of coins whose values add up to {} is {}".format(amount, change_making_dp(denomination, amount)))
print("The optimal combination is:\n", combination)