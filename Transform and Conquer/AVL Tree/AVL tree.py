"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of AVL tree
# three operations: search, insert and remove
# for each insertion and deletion,
# balance factor is calculated for each node it passes through
# if the absolute value of balance factor is greater than 1,
# the corresponding rotation operation will be done to balance the tree
# so the time complexity for all three operations are Θ(nlog n)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0  # initialize the height to 0
class AVL_Tree(object):
    def __init__(self):
        self.root = None
    # calculate height
    def calc_height(self, node):
        if not node:
            return -1
        return node.height
    # calculate balance factor
    def calc_balance_factor(self, node):
        if not node:
            return 0
        return self.calc_height(node.left) - self.calc_height(node.right)
    # left_rotation, symmetric to right rotation
    def left_rotation(self, node):
        """
                A                    C
               / \                  / \
              B   C     ------>    A   E
                 / \              / \
                D   E            B   D
        """
        t1 = node.right
        t2 = t1.left
        # reconstruction
        t1.left = node
        node.right = t2
        # update the height of node and t1
        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        t1.height = max(self.calc_height(t1.left), self.calc_height(t1.right)) + 1
        return t1
    # right rotation, symmetric to left rotation
    def right_rotation(self, node):
        """
                A                    B
               / \                  / \
              B   C     ------>    D   A
             / \                      / \
            D   E                    E   C
        """
        t1 = node.left
        t2 = t1.right
        # reconstruction
        t1.right = node
        node.left = t2
        # update the height of node and t1
        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        t1.height = max(self.calc_height(t1.left), self.calc_height(t1.right)) + 1
        return t1
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
    def insert(self, value):
        node = Node(value)  # create a new node
        self.root = self.insert_node(self.root, node)
    def insert_node(self, root, node):
        if not root:
            return node
        if node.value < root.value:
            root.left = self.insert_node(root.left, node)
        else:
            root.right = self.insert_node(root.right, node)
        root.height = max(self.calc_height(root.left), self.calc_height(root.right)) + 1  # update height
        return self.settle_violation(root)
    def settle_violation(self, root):
        balance = self.calc_balance_factor(root)
        if balance > 1:
            # case 1: double-right rotation
            if self.calc_balance_factor(root.left) >= 0:
                return self.right_rotation(root)
            # case 2: left-right rotation
            else:
                root.left = self.left_rotation(root.left)
                return self.right_rotation(root)
        elif balance < -1:
            # case 3: double-left rotation
            if self.calc_balance_factor(root.right) <= 0:
                return self.left_rotation(root)
            # case 4: right-left rotation
            else:
                root.right = self.right_rotation(root.right)
                return self.left_rotation(root)
        return root
    def remove(self, value):
        # throw an exception if root is null
        if not self.root:
            raise ValueError("The tree is null")
        self.root = self.remove_node(self.root, value)
    def remove_node(self, root, value):
        if not root:
            return root
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
                temp = self.get_max(root.left)
                root.value = temp.value
                root.left = self.remove_node(root.left, temp.value)
        root.height = max(self.calc_height(root.left), self.calc_height(root.right)) + 1  # update height
        return self.settle_violation(root)
    def get_max(self, root):
        if root.right:
            return self.get_max(root.right)
        return root

    def traversal(self):
        if not self.root:
            raise ValueError("The tree is null!")
        return self.in_order(self.root)
    def in_order(self, root):
        if root.left:
            self.in_order(root.left)
        print(root.value, end=' ')
        if root.right:
            self.in_order(root.right)

# instantiate an AVL tree
avl = AVL_Tree()

array = [1, 3, 2, 4, 5, 7, 6]

# insertion
# binary search tree
"""
       1
        \ 
         3
        / \ 
       2   4
            \ 
             5
              \ 
               7
              /
             6 
"""

for element in array:
    avl.insert(element)

# AVL tree
"""
      4
     / \ 
    2   6
   / \ / \ 
  1  3 5  7
"""
print("After insertion:")
avl.traversal()

# search
key1 = 6; key2 = 8
print("\nSearch: ")

# success
print("search key = %d" % key1)
if avl.search(key1):
    print("Search successful.")
else:
    print("Search unsuccessful.")

# fail
print("search key = %d" % key2)
if avl.search(key2):
    print("Search successful.")
else:
    print("Search unsuccessful.")

# deletion
avl.remove(6)
avl.remove(5)
avl.remove(7)


# After deletion
"""
     2
    / \ 
   1   4
      /
     3 
"""

print("After deleting 6, 5 and 7:")
avl.traversal()

