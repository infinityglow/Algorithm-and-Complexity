"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of knapsack problem solved by brute-force approach

def power_set_gen(w):
    p_set = [set()]
    for item in w:
        temp_set = []
        for subset in p_set:
            subset = subset | {item}
            temp_set.append(subset)
        p_set.extend(temp_set)
    return p_set

def knapsack_bf(w_v, p_set, W):
    w_combination = None; max_value = 0
    for instance in p_set:
        weight, value = 0, 0
        for item in instance:
            weight += item; value += w_v[item]
        if weight <= W and value > max_value:
            w_combination = instance
            max_value = value
    return w_combination, max_value


w_v = {7: 42, 3: 12, 4: 40, 5: 25}  # mapping from weight to value
w_i = {7: 1, 3: 2, 4: 3, 5: 4}  # mapping from weight to index
W = 10

power_set = power_set_gen(w_v.keys())
combination, max_value = knapsack_bf(w_v, power_set, W)
combination = list(combination)

print("The optimal combination is: ")
for i in range(len(combination)-1):
    print("  item %d" % w_i[combination[i]], end=', ')
print("item %d." % w_i[combination[-1]])
print("The total value is %d." % max_value)



