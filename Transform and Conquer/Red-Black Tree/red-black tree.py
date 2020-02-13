"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of red-black tree
# three operations: search, insert and remove
# the following properties must be satisfied for each insertion and deletion:
#   1. each node is either red or black
#   2. the root node must be black
#   3. All leaf nodes(NIL) are black
#   4. if a node is red, both its children are black(including NIL)
#   5. Every path from a given node to its descendent NIL contains the same number of black nodes.
# if the properties are violated, then rotation or color rearranging are performed to balance the tree,
# so the time complexity for all three operations are close to Θ(nlog n)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.color = 'r'
        self.left = None
        self.right = None
        self.parent = None
    # get the grandparent node
    def grandparent(self):
        if not self.parent:
            return None
        return self.parent.parent
    # get the uncle node
    def uncle(self):
        if not self.grandparent():
            return None
        if self.parent is self.grandparent().left:
            return self.grandparent().right
        else:
            return self.grandparent().left
    # get the brother node
    def brother(self):
        if self.parent.left is self:
            return self.parent.right
        else:
            return self.parent.left

class Red_Black_Tree(object):
    def __init__(self):
        # construct a NIL node
        NIL = Node(None)
        NIL.color = 'b'
        self.NIL = NIL
        self.root = None
    def left_rotation(self, node):
        """
                g                       g
               / \                     / \
              ?   p                   ?   n
                 / \      -------->      / \
                ?   n                   p   r
                   / \                 / \
                  l   r               ?   l
        g: grandparent, p: parent, n: rotated node, l: left child, r: right child
        """
        if not node.parent:
            self.root = node
            return
        grandparent = node.grandparent()
        parent = node.parent
        t = node.left
        parent.right = t

        if t is not self.NIL:
            t.parent = parent
        node.left = parent
        parent.parent = node

        if parent is self.root:
            self.root = node
        node.parent = grandparent

        if grandparent:
            # left sub-tree
            if grandparent.left is parent:
                grandparent.left = node
            # right sub-tree
            else:
                grandparent.right = node
    def right_rotation(self, node):
        """
                g                      g
               / \                    / \
              p   ?                  n   ?
             / \      -------->     / \
            n   ?                  l   p
           / \                        / \
          l   r                      r   ?
        g: grandparent, p: parent, n: rotated node, l: left child, r: right child
        """
        if not node.parent:
            self.root = node
            return
        grandparent = node.grandparent()
        parent = node.parent
        t = node.right
        parent.left = t

        if t is not self.NIL:
            t.parent = parent
        node.right = parent
        parent.parent = node

        if parent is self.root:
            self.root = node
        node.parent = grandparent

        if grandparent:
            # left sub-tree
            if grandparent.left is parent:
                grandparent.left = node
            # right sub-tree
            else:
                grandparent.right = node
    def search(self, value):
        # throw an exception if root is null
        if not self.root:
            raise ValueError("The tree is null")
        return self.search_node(self.root, value)
    def search_node(self, root, value):
        if root is self.NIL:  # return None if the node is NIL
            return None
        if value < root.value:  # search from the left sub-tree
            return self.search_node(root.left, value)
        elif value > root.value:  # search from the right sub-tree
            return self.search_node(root.right, value)
        else:
            return root
    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        if not self.root:
            self.root = new_node
            new_node.color = 'b'  # set root's color to black
        else:
            self.insert_node(self.root, new_node)
    def insert_node(self, root, node):
        if node.value < root.value:
            if root.left is not self.NIL:
                self.insert_node(root.left, node)
            else:
                root.left = node
                node.parent = root
                self.insert_case(node)
        else:
            if root.right is not self.NIL:
                self.insert_node(root.right, node)
            else:
                root.right = node
                node.parent = root
                self.insert_case(node)
    def insert_case(self, node):
        # case 1: the root's color is red
        if not node.parent:
            self.root = node
            node.color = 'b'
            return
        # case 2: parent and uncle are red, grandparent is black
        """
                    g(b)                      g(r)
                   /    \                    /    \ 
                 p(r)   u(r)   -------->   p(b)   u(b)  
                 /                          /
               n(r)                       n(r)
        """
        if node.parent.color == 'r':
            if node.uncle().color == 'r':
                node.parent.color = 'b'; node.uncle().color = 'b'
                node.grandparent().color = 'r'
                self.insert_case(node.grandparent())  # call insert_case() recursively
            else:
                # case 3A: uncle is black or NIL, new node is the right child of parent, parent is the left child of grandparent
                if node.parent.right is node and node.parent is node.grandparent().left:
                    """
                            g(b)                    g(b)                    n(b)
                           /    \                  /    \                  /    \   
                         p(r)   u(b)   ------>   n(r)   u(b)   ------>   p(r)   g(r)
                           \                      /                               \ 
                           n(r)                 p(r)                             u(b)
                    """
                    node.color = 'b'
                    node.grandparent().color = 'r'
                    self.left_rotation(node)
                    self.right_rotation(node)
                # case 3B: uncle is black or NIL, new node is the left child of parent, parent is the right child of grandparent
                elif node.parent.left is node and node.parent is node.grandparent().right:
                    """
                            g(b)                    g(b)                    n(b)
                           /    \                  /    \                  /    \   
                         u(b)   p(r)   ------>   u(b)   n(r)   ------>   g(r)   p(r)
                                /                         \               / 
                              n(r)                        p(r)          u(b)
                    """
                    node.color = 'b'
                    node.grandparent().color = 'r'
                    self.right_rotation(node)
                    self.left_rotation(node)
                # case 4A: uncle is black or NIL, new node is the left child of parent, parent is the left child of grandparent
                elif node.parent.left is node and node.parent is node.grandparent().left:
                    """
                            g(b)                    p(b)
                           /    \                  /    \   
                         p(r)   u(b)   ------>   n(r)   g(r)
                          /                               \ 
                        n(r)                             u(b)
                    """
                    node.parent.color = 'b'
                    node.grandparent().color = 'r'
                    self.right_rotation(node.parent)
                # case 4B: uncle is black or NIL, new node is the right child of parent, parent is the left child of grandparent
                elif node.parent.right is node and node.parent is node.grandparent().right:
                    """
                            g(b)                    p(b)
                           /    \                  /    \   
                         u(b)   p(r)   ------>   g(r)   n(r)
                                  \               / 
                                  n(r)          u(b)
                    """
                    node.parent.color = 'b'
                    node.grandparent().color = 'r'
                    self.left_rotation(node.parent)
    def remove(self, value):
        # throw an exception if root is null
        if not self.root:
            raise ValueError("The tree is null")
        self.remove_node(self.root, value)
    def remove_node(self, root, value):
        if root is self.NIL:
            return
        # search
        if value < root.value:
            self.remove_node(root.left, value)
        elif value > root.value:
            self.remove_node(root.right, value)
        else:
            # no children
            if root.left is self.NIL and root.right is self.NIL:
                self.remove_leaf(root, True)
            # either left child or right child
            elif root.left is self.NIL or root.right is self.NIL:
                self.remove_one_child(root)
            # both left child and right child
            else:
                temp = self.get_max(root.left)  # find the maximum value from the left sub-tree
                root.value = temp.value
                self.remove_node(root.left, temp.value)
    def remove_leaf(self, node, flag):
        # remove red node without any change
        if node.color == 'r':
            self.fix(node, self.NIL)
            return
        # black node
        # case 1: node to be removed is the root
        if node is self.root:
            if flag:
                self.fix(node, None)
            return
        else:
            parent = node.parent
            brother = node.brother()
            # case 2: brother node is red
            if brother.color == 'r':
                parent.color = 'r'; brother.color = 'b'
                # case 2A: node to be removed is the left child of parent
                if node.parent.left is node:
                    """
                            p(r)                              b(b)
                           /    \                            /    \ 
                         n(b)   b(r)        -------->      p(r)   r(b)   
                         /  \   /  \                       /  \ 
                        N    N l(b) r(b)                 n(b) l(b)
                                                         /  \ 
                                                        N    N
                    """
                    self.left_rotation(brother)
                # case 2B: node to be removed is the right child of parent
                else:
                    """
                            p(r)                              b(b)
                           /    \                            /    \ 
                         b(r)   n(b)        -------->      l(b)   p(r)   
                        /   \    / \                              /  \ 
                     l(b)  r(b) N   N                           r(b) n(b)
                                                                     /  \ 
                                                                    N    N
                    """
                    self.right_rotation(brother)
                self.remove_leaf(node, True)
            else:
                nephew_left = brother.left
                nephew_right = brother.right
                # case 3A: brother node is black, right nephew node is red, node to be removed is the left child of parent
                if node.parent.left is node and nephew_right.color == 'r':
                    """
                            p(?)                              b(?)                             b(?)
                           /    \                            /    \                           /    \ 
                         n(b)   b(b)        -------->      p(b)   r(b)        -------->     p(b)   r(b)          
                         /  \   /  \                       /  \                             /  \ 
                        N    N l(?) r(r)                 n(b) l(?)                         N   l(?)
                                                         /  \ 
                                                        N    N
                    """
                    brother.color = parent.color; parent.color = 'b'; nephew_right.color = 'b'
                    self.left_rotation(brother)
                # case 3B: brother node is black, left nephew node is red, node to be removed is the right child of parent
                elif node.parent.right is node and nephew_left.color == 'r':
                    """
                            p(?)                              b(?)                             b(?)
                           /    \                            /    \                           /    \  
                         b(b)   n(b)        -------->      l(b)   p(b)        -------->     l(b)   p(b)    
                        /   \    / \                              /  \                             /  \ 
                     l(r)  r(?) N   N                           r(?) n(b)                        r(?)  N
                                                                     /  \ 
                                                                    N    N
                    """
                    brother.color = parent.color; parent.color = 'b'; nephew_left.color = 'b'
                    self.right_rotation(brother)
                # case 4A: brother node is black, left nephew node is red, node to be removed is the left child of parent
                elif node.parent.left is node and nephew_left.color == 'r':
                    """
                            p(?)                              p(?)                             l(?)
                           /    \                            /    \                           /    \ 
                         n(b)   b(b)        -------->      n(b)   l(b)        -------->     p(b)   b(b)          
                         /  \   /  \                       /  \   /  \                         \   /  \ 
                        N    N l(r) N                     N    N ?   b(r)                       ? ?    N
                               /  \                                  /  \ 
                              ?    ?                                ?    N
                    """
                    nephew_left.color = 'b'; brother.color = 'r'
                    self.right_rotation(nephew_left)
                    self.remove_leaf(node, True)
                # case 4B: brother node is black, right nephew node is red, node to be removed is the right child of parent
                elif node.parent.right is node and nephew_right.color == 'r':
                    """
                            p(?)                              p(?)                             r(?)
                           /    \                            /    \                           /    \  
                         b(b)   n(b)        -------->      r(b)   n(b)        -------->     b(b)   p(b)    
                         /  \    / \                       /  \    / \                      /  \   / 
                        N  r(r) N   N                   b(r)   ?  N   N                    N    ? ?
                           /  \                         /  \ 
                          ?    ?                       N    ?
                    """
                    nephew_right.color = 'b'; brother.color = 'r'
                    self.left_rotation(nephew_right)
                    self.remove_leaf(node, True)
                # case 5: brother node is black, and both of its children are NIL
                elif brother.left.color == 'b' and brother.right.color == 'b':
                    # case 5A: parent node is red
                    if parent.color == 'r':
                        """
                                p(r)                              p(b)                             p(b)
                               /    \                            /    \                           /    \  
                             n(b)   b(b)        -------->      n(b)   b(r)        -------->      N     b(r)    
                             /  \   /  \                       /  \   /  \                             /  \ 
                            N    N N    N                     N    N N    N                           N    N
                        """
                        parent.color = 'b'; brother.color = 'r'
                    # case 5B: parent node is black
                    else:
                        """
                                p(b)                              p(b)
                               /    \                            /    \ 
                             n(b)   b(b)        -------->      n(b)   b(r)    
                             /  \   /  \                       /  \   /  \ 
                            N    N N    N                     N    N N    N
                        """
                        brother.color = 'r'
                        self.remove_leaf(parent, False)
        if flag:
            self.fix(node, self.NIL)

    def remove_one_child(self, node):
        if node.left is not self.NIL:
            node.left.color = 'b'
            self.fix(node, node.left)
        else:
            node.right.color = 'b'
            self.fix(node, node.right)
    def fix(self, p, n):
        # p.parent is None
        if not p.parent:
            self.root = n
        elif p.parent.left is p:
            p.parent.left = n
        elif p.parent.right is p:
            p.parent.right = n
        if n is not self.NIL and n is not None:
            n.parent = p.parent
        del p

    def get_max(self, root):
        if root.right is not self.NIL:
            return self.get_max(root.right)
        return root
    def traversal(self):
        collection = {}
        if self.root:
            return self.in_order(self.root, collection)
        return collection
    def in_order(self, root, collection):
        if root.left is not self.NIL:
            self.in_order(root.left, collection)
        collection[root.value] = root.color
        if root.right is not self.NIL:
            self.in_order(root.right, collection)
        return collection


# instantiate an empty red-black tree
rbt = Red_Black_Tree()

array = [1, 3, 4, 2, 5, 7, 6]

# insertion
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
    rbt.insert(element)

# red-black tree
"""
      3(b)
     /    \ 
  1(b)    5(r)
    \     /  \ 
   2(r) 4(b) 7(b)
             /
           6(r) 
"""
print("After insertion:")
print(rbt.traversal())

# search
key1 = 6; key2 = 8
print("Search: ")

# success
print("search key = %d" % key1)
if rbt.search(key1):
    print("Search successful.")
else:
    print("Search unsuccessful.")

# fail
print("search key = %d" % key2)
if rbt.search(key2):
    print("Search successful.")
else:
    print("Search unsuccessful.")

# deletion
rbt.remove(5)
rbt.remove(1)
rbt.remove(7)

# After deletion
"""
     3(b)
    /    \ 
  2(b)   6(b)
         /
       4(r) 
"""

print("After deleting 5, 1 and 7:\n", rbt.traversal())
