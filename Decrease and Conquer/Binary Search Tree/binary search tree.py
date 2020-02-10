"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of binary search tree
# three operations: search, insert and remove
# time complexity is determined by the structure of the tree
# if the tree is well-balanced, complexity is close to Θ(log n)
# while the complexity can be degraded to linear Θ(n),
# if the tree is constructed by the successive insertions of increasing or decreasing keys

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
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
    def search(self, value):
        # throw an exception if root is null
        if not self.root:
            raise ValueError("The tree is null")
        return self.search_node(self.root, value)
    def search_node(self, root, value):
        if not root:  # return None if the node is null
            return None
        if value < root.value:  # search from the left sub-tree
            return self.search_node(root.left, value)
        elif value > root.value:  # search from the right sub-tree
            return self.search_node(root.right, value)
        else:
            return root
    def get_max(self, root):
        if root.right:
            return self.get_max(root.right)
        return root
    def remove(self, value):
        # throw an exception if root is null
        if not self.root:
            raise ValueError("The tree is null")
        self.root = self.remove_node(self.root, value)
    def remove_node(self, root, value):
        if not root:
            return None
        # search
        if value < root.value:
            root.left = self.remove_node(root.left, value)
        elif value > root.value:
            root.right = self.remove_node(root.right, value)
        else:
            # no children
            if not root.left and not root.right:
                del root
                return None
            # either left child or right child
            elif not root.left:
                temp = root.right
                del root
                return temp
            elif not root.right:
                temp = root.left
                del root
                return temp
            # both left and right child
            else:
                temp = self.get_max(root.left)  # find the maximum value from the left sub-tree
                root.value = temp.value
                root.left = self.remove_node(root.left, temp.value)
        return root
    def traversal(self):
        collection = []
        if self.root:
            return self.traversal_tree(self.root, collection)
        return collection
    def traversal_tree(self, root, collection):
        # in-order traversal
        if root.left:
            self.traversal_tree(root.left, collection)
        collection.append(root.value)
        if root.right:
            self.traversal_tree(root.right, collection)
        return collection

array = [48, 25, 73, 10, 34, 61, 81]
bst = BST()
# build binary search tree
for element in array:
    bst.insert(element)
print("Build binary search tree: \n", bst.traversal())
# search
key1 = 61; key2 = 89
print("Search: ")

# success
print("search key = %d" % key1)
if bst.search(key1):
    print("Search successful.")
else:
    print("Search unsuccessful.")

# fail
print("search key = %d" % key2)
if bst.search(key2):
    print("Search successful.")
else:
    print("Search unsuccessful.")

# insertion
bst.insert(42)
print("After insertion: \n", bst.traversal())

# deletion
# case 1
bst.remove(10)
print("After deleting 10: \n", bst.traversal())

# case 2
bst.remove(34)
print("After deleting 34: \n", bst.traversal())

# case 3
bst.remove(48)
print("After deleting 48: \n", bst.traversal())

