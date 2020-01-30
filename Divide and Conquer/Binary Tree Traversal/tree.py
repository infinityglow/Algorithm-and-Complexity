"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# build a binary tree for traversal

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class tree(object):
    def __init__(self):
        self.root = None
    def insert(self, value):
        new_node = Node(value)  # create a new node
        # check whether the root node is null
        if not self.root:  # search from the left sub-tree
            self.root = new_node
        else:  # search from the right sub-tree
            self.insert_node(self.root, new_node)
    def insert_node(self, root, node):
        if node.value < root.value:
            if root.left:
                self.insert_node(root.left, node)
            else:
                root.left = node
        else:
            if root.right:
                self.insert_node(root.right, node)
            else:
                root.right = node


array = [48, 25, 73, 10, 34, 61, 81]
bst = tree()
# build binary search tree
for element in array:
    bst.insert(element)
