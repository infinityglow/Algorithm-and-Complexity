"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

#  sequential list (linked list implementation) and its three operations: Search, Insert and Remove
#  complexity: search Θ(n), insert Θ(1) remove Θ(1)

class Node(object):
    def __init__ (self, value):
        self.value = value
        self.next = None

class Linked_List(object):
    def __init__(self):
        self.length = 0
        self.header = None
    def search(self, value):
        p = self.header  # retrieve the first node
        while p != None:
            if p.value == value:
                return p
            p = p.next
        return None
    def insert(self, value):
        # instantiate a new node
        p = Node(value)
        p.next = self.header
        self.header = p
        self.length += 1
    def remove(self):
        p = self.header  # retrieve the first node
        if p is not None:
            self.header = p.next
            self.length -= 1
            del p  # delete node p
    def traversal(self):
        array = []  # for displaying
        p = self.header
        while p is not None:
            array.append(p.value)
            p = p.next
        return array


elements = [24, 22, 76, 41, 7, 61, 15, 34, 80]
# initialize an empty linked list
linked_list = Linked_List()
# construct linked list
for e in elements:
    linked_list.insert(e)
print("The original array: \n", linked_list.traversal())
# search node 61
print("Search node 61:")
if linked_list.search(61):
    print("Search is successful!")
else:
    print("Search is unsuccessful!")
# remove a node
linked_list.remove()
print("After removing a node: \n", linked_list.traversal())
# insert node 80
linked_list.insert(80)
print("After inserting node 34: \n", linked_list.traversal())

