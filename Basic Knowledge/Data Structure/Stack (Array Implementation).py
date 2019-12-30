"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of stack and its two operations: Push and Pop

class Stack (object):

    def __init__ (self, top, down, array):
        self.array = array
        self.top = top
        self.down = down

    def push(self, element):
        # examine overflow
        if self.top >= len(self.array) - 1:
            raise IndexError("Stack overflow!")
        else:
            self.top += 1  # increment top by 1
            self.array[self.top] = element
        return

    def pop(self):
        # examine underflow
        if self.top <= 0:
            raise IndexError("Stack underflow!")
        else:
            self.array[self.top] = None
            self.top -= 1  # decrement top by 1
        return


array = [24, 22, 76, 41, 7, 61, 15, 34, 80, None, None, None, None]
down = 0; top = 8
stack = Stack(top, down, array)  # instantiate a stack
print("The original array: \n", stack.array)
# push 24, 85 into the stack
stack.push(24); stack.push(85)
print("After pushing 24 and 85: \n", stack.array)
# pop three elements
stack.pop(); stack.pop(); stack.pop()
print("After popping three elements: \n", stack.array)
