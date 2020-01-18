"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

import random

# array generator for different cases (best case, average case, worst case)

class generator(object):
    def __init__(self, size, seed):
        self.size = size
        random.seed = seed  # for reproducibility
    def avg(self):
        return [random.randint(0,self.size) for i in range(self.size)]
    def best(self):
        return sorted([random.randint(0,self.size) for i in range(self.size)])
    def worst(self):
        return sorted([random.randint(0,self.size) for i in range(self.size)], reverse=True)


