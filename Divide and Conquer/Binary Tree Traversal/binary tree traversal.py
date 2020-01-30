"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of binary tree traversal
# pre-order: root node -> left sub-tree -> right sub-tree
# in-order: left sub-tree -> root node -> right sub-tree
# post-order: left sub-tree -> right sub-tree -> root node
# time complexity: Θ(n)

from tree import bst as T

# pre-order
def pre_order(T):
    print(T.value, end=' ')
    if T.left:
        pre_order(T.left)
    if T.right:
        pre_order(T.right)

# in-order
def in_order(T):
    if T.left:
        pre_order(T.left)
    print(T.value, end=' ')
    if T.right:
        pre_order(T.right)

# post-order
def post_order(T):
    if T.left:
        pre_order(T.left)
    if T.right:
        pre_order(T.right)
    print(T.value, end=' ')


print("pre-order traversal: ")
pre_order(T.root)
print("\nin-order traversal: ")
in_order(T.root)
print("\npost-order traversal: ")
post_order(T.root)