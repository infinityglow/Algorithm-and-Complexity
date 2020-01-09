"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of queue and its two operations: Enqueue and Dequeue

class Queue (object):

    def __init__ (self, front, rear, array):
        self.array = array
        self.front = front
        self.rear = rear

    def enqueue(self, element):
        # examine overflow
        if self.rear >= len(self.array) - 1:
            raise IndexError("Queue overflow! ")
        else:
            self.rear += 1  # increment top by 1
            self.array[self.rear] = element
        return

    def dequeue(self):
        # examine underflow
        if self.front >= self.rear:
            raise IndexError("Queue underflow!")
        else:
            self.array[self.front] = None
            self.front += 1  # decrement top by 1
        return


array = [24, 22, 76, 41, 7, 61, 15, 34, 80, None, None, None, None]
front = 0; rear = 8
queue = Queue(front, rear, array)  # instantiate a queue
print("The original array: \n", queue.array)
# enqueue 24, 85 into the queue
queue.enqueue(24); queue.enqueue(85)
print("After enqueuing 24 and 85: \n", queue.array)
# dequeue three elements
queue.dequeue(); queue.dequeue(); queue.dequeue()
print("After dequeuing three elements: \n", queue.array)

