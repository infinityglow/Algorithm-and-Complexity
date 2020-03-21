"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of 2-3 tree
# three operations: search, insert and remove
# each node has either one element or two elements
# insertion operation is always occurred in the leaf node
# when node is not full, put the item into the node, otherwise, split node into two new nodes,
# and the procedure is done recursively until meeting the root node
# deletion is similar to binary search tree, but it has several different cases:
#   case 1: delete 3-node, delete without any adjustment
#   case 2: brother node is full, borrow one element and balance the tree
#   case 3: parent node is full, borrow one element from the parent node, so parent node decreases to 2-node
#   case 4: neither brother node nor parent node is not full, merge parent node and brother node,
#   and check parent node recursively until encountering the root node
# time complexity: Θ(log n), in the range of [log2_n, log3_n]

class Node(object):
    def __init__(self, value):
        self.value1 = value
        self.value2 = None
        self.left = None
        self.mid = None
        self.right = None
        self.parent = None
    def is_leaf(self):
        # whether node is leaf node
        return not self.left and not self.mid and not self.right
    def is_full(self):
        # whether node is 3-node
        return self.value2 is not None
    def get_child(self, value):
        # given a value, return its child to be searched
        if self.value2:  # 3-node
            if value < self.value1:
                return self.left
            elif value < self.value2:
                return self.mid
            return self.right
        else:  # 2-node
            if value < self.value1:
                return self.left
            return self.right
    # return 3-node brother node
    def brother(self):
        # only return brother when parent is not null
        if self.parent:
            # parent node is 2-node
            if not self.parent.is_full():
                if self.parent.left is self:
                    return self.parent.right
                return self.parent.left
            # parent node is 3-node
            else:
                if self.parent.mid is self:
                    if self.parent.right.is_full():
                        return self.parent.right
                    if self.parent.left.is_full():
                        return self.parent.left
                    # choose arbitrarily
                    return self.parent.right
                return self.parent.mid

class TwoThreeTree(object):
    def __init__(self):
        self.root = None
    def search(self, value):
        # throw an exception if root is null
        if not self.root:
            raise ValueError("The tree is null")
        return self.search_node(self.root, value)
    def search_node(self, root, value):
        if not root:
            return None  # return None if the node is null
        if value == root.value1 or value == root.value2:
            return root
        return self.search_node(root.get_child(value), value)  # search from the expected sub-tree
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        self.insert_node(self.root, value)
    def insert_node(self, root, value):
        # search until `root` is leaf node
        while not root.is_leaf():
            root = root.get_child(value)
        # node is 2-node
        if not root.is_full():
            self.put_item(root, value)
        # node is 3-node
        else:
            self.put_item_full(root, value)
    def put_item(self, leaf, value):
        if value < leaf.value1:
            leaf.value2 = leaf.value1
            leaf.value1 = value
        else:
            leaf.value2 = value
    def put_item_full(self, leaf, value):
        """
        :param leaf: leaf node which is full
        :param value: value to be inserted
        :return: value that needs to be pushed upward, and splitting node
        """
        pvalue, new_node = self.split(leaf, value)
        # iterate from leaf up to root
        while leaf.parent:
            # insert value into the parent node if parent node is 2-node, then jump out of `while` loop
            if not leaf.parent.is_full():
                self.put_item(leaf.parent, pvalue)
                # leaf is the parent's left child
                if leaf.parent.left is leaf:
                    leaf.parent.mid = new_node
                # leaf is the parent's right child
                else:
                    leaf.parent.mid = leaf; leaf.parent.right = new_node
                new_node.parent = leaf.parent
                break
            # split parent node and rearrange each node's references accordingly
            else:
                pvalue_p, new_node_p = self.split(leaf.parent, pvalue)
                # case 1: splitting node is the parent's left child
                if leaf.parent.left is leaf:
                    """
                                                     4
                       4 6                          / \ 
                      / | \        insert 3        2   6      
                    1 2 5  7      --------->      / \ / \    
                                                 1  3 5  7
                    """
                    new_node_p.left = leaf.parent.mid; leaf.parent.mid.parent = new_node_p
                    new_node_p.right = leaf.parent.right; leaf.parent.right.parent = new_node_p
                    leaf.parent.right = new_node; new_node.parent = leaf.parent
                # case 2: splitting node is the parent's middle child
                elif leaf.parent.mid is leaf:
                    """
                                                     4
                       2 6                          / \ 
                      / | \        insert 5        2   6      
                     1 3 4 7      --------->      / \ / \    
                                                 1  3 5  7
                    """
                    new_node_p.left = new_node; new_node.parent = new_node_p
                    new_node_p.right = leaf.parent.right; leaf.parent.right.parent = new_node_p
                    leaf.parent.right = leaf.parent.mid
                # case 3: splitting node is the parent's right child
                else:
                    """
                                                      4
                       2 4                           / \ 
                      / | \         insert 7        2   6      
                     1  3 5 6      --------->      / \ / \    
                                                  1  3 5  7
                    """
                    leaf.parent.right = leaf.parent.mid; temp = leaf.parent.right
                    new_node_p.left = leaf; leaf.parent = new_node_p
                    new_node_p.right = new_node; new_node.parent = new_node_p
                    leaf = temp
                leaf.parent.mid = None  # convert to 2-node
                leaf = leaf.parent; pvalue = pvalue_p; new_node = new_node_p  # move `leaf`, `pvalue`, `new_node` upward
        # if pushing forward to the root node, a new root node is created
        else:
            new_root = Node(pvalue)
            new_root.left = leaf; new_root.right = new_node
            leaf.parent = new_root; new_node.parent = new_root
            self.root = new_root
    def split(self, leaf, value):
        new_node = Node(None)
        # `value1` to be pushed upward
        if value < leaf.value1:
            pvalue = leaf.value1
            leaf.value1 = value
            new_node.value1 = leaf.value2
        # `value` to be pushed upward
        elif value < leaf.value2:
            pvalue = value
            new_node.value1 = leaf.value2
        # `value2` to be pushed upward
        else:
            pvalue = leaf.value2
            new_node.value1 = value
        leaf.value2 = None
        return pvalue, new_node
    def remove(self, value):
        # throw an exception if root is null
        if not self.root:
            raise ValueError("The tree is null")
        node = self.search(value)  # find the node to be removed
        # leaf node
        if node.is_leaf():
            self.remove_leaf(node, value)
        # parent node
        else:
            # find predecessor from the middle sub-tree
            if node.is_full() and node.value2 == value:
                predecessor = self.get_predecessor(node.mid)
                # swap
                if predecessor.is_full():
                    predecessor.value2, node.value2 = node.value2, predecessor.value2
                else:
                    predecessor.value1, node.value2 = node.value2, predecessor.value1
            # find predecessor from the left sub-tree
            else:
                predecessor = self.get_predecessor(node.left)
                # swap
                if predecessor.is_full():
                    predecessor.value2, node.value1 = node.value1, predecessor.value2
                else:
                    predecessor.value1, node.value1 = node.value1, predecessor.value1
            self.remove_leaf(predecessor, value)
    def get_predecessor(self, root):
        if root.right:
            return self.get_predecessor(root.right)
        return root
    def remove_leaf(self, node, value):
        # delete without any adjustment
        if node.is_full():
            self.remove_item(node, value)
        else:
            brother = node.brother()
            while node.parent:
                # case 1
                if brother.is_full():
                    self.leaf_case1(node, brother)
                    break
                else:
                    # case 2
                    if node.parent.is_full():
                        self.leaf_case2(node, brother)
                        break
                    # case 3
                    else:
                        node = self.merge(node, brother)
                        brother = node.brother()
            else:
                self.root = node.mid
                del node
    def remove_item(self, node, value):
        # suppose node is full
        if node.value1 == value:
            node.value1 = node.value2
        node.value2 = None
    def leaf_case1(self, node, brother):
        node.value1 = None
        if node is node.parent.left:
            node.value1 = node.parent.value1
            node.parent.value1 = brother.value1
            # brother node has children
            if brother.left:
                """
                       2 5         remove 1        3 5          
                      / | \       --------->      / | \ 
                     1 3 4 6                     2  4  6
                """
                node.left = node.mid
                node.right = brother.left
                brother.left.parent = node
                brother.left = brother.mid
            self.remove_item(brother, brother.value1)
        elif node is node.parent.right:
            """
                       2 5         remove 6        2 4          
                      / | \       --------->      / | \ 
                     1 3 4 6                     1  3  5
            """
            if node.parent.is_full():
                node.value1 = node.parent.value2
                node.parent.value2 = brother.value2
            else:
                node.value1 = node.parent.value1
                node.parent.value1 = brother.value2
            # brother node has children
            if brother.right:
                node.right = node.mid
                node.left = brother.right
                brother.right.parent = node
                brother.right = brother.mid
            self.remove_item(brother, brother.value2)
        else:
            if brother is node.parent.right:
                """
                       2 4         remove 3        2 5          
                      / | \       --------->      / | \ 
                     1  3 5 6                    1  4  6
                """
                node.value1 = node.parent.value2
                node.parent.value2 = brother.value1
                # brother node has children
                if brother.left:
                    node.left = node.mid
                    node.right = brother.left
                    brother.left.parent = node
                    brother.left = brother.mid
                self.remove_item(brother, brother.value1)
            else:
                """
                       3 5         remove 4        2 5          
                      / | \       --------->      / | \ 
                    1 2 4  6                     1  3  6
                """
                node.value1 = node.parent.value1
                node.parent.value1 = brother.value2
                # brother node has children
                if brother.right:
                    node.right = node.mid
                    node.left= brother.right
                    brother.right.parent = node
                    brother.right = brother.mid
                self.remove_item(brother, brother.value2)
        brother.mid = None
        node.mid = None
    def leaf_case2(self, node, brother):
        node.value1 = None
        if node is node.parent.left:
            """
                       2 4         remove 1         4          
                      / | \       --------->       / \ 
                     1  3  5                     2 3  5
            """
            self.put_item(brother, node.parent.value1)
            if node.mid:
                brother.mid = brother.left
                brother.left = node.mid
                node.mid.parent = brother
            node.parent.left = brother
            self.remove_item(node.parent, node.parent.value1)
        elif node is node.parent.right:
            """
                       2 4         remove 5         2          
                      / | \       --------->       / \ 
                     1  3  5                      1  3 4            
            """
            self.put_item(brother, node.parent.value2)
            if node.mid:
                brother.mid = brother.right
                brother.right = node.mid
                node.mid.parent = brother
            node.parent.right = brother
            self.remove_item(node.parent, node.parent.value2)
        else:
            """
                       2 4         remove 3         2          
                      / | \       --------->       / \ 
                     1  3  5                      1  4 5            
            """
            self.put_item(brother, node.parent.value2)
            if node.mid:
                brother.mid = brother.left
                brother.left = node.mid
                node.mid.parent = brother
            self.remove_item(node.parent, node.parent.value2)
        node.parent.mid = None
        del node
    def merge(self, node, brother):
        self.put_item(brother, node.parent.value1)
        if node is node.parent.left:
            """
                        4                          4
                       / \                       /   \ 
                      2   6        remove 1     ?     6              
                     / \ / \      --------->    |    / \          
                    1  3 5  7                  2 3  5   7                              
            """
            if node.mid:
                brother.mid = brother.left
                brother.left = node.mid
                node.mid.parent = brother
            node.parent.right = None
        else:
            """
                        4                          4
                       / \                       /   \ 
                      2   6        remove 7     2     ?              
                     / \ / \      --------->   / \    |      
                    1  3 5  7                 1   3  5 6          
            """
            if node.mid:
                brother.mid = brother.right
                brother.right = node.mid
                node.mid.parent = brother
            node.parent.left = None
        node.parent.mid = brother
        temp = node
        node = node.parent
        del temp
        return node
    def traversal(self):
        if not self.root:
            raise ValueError("The tree is null!")
        return self.in_order(self.root)
    def in_order(self, root):
        if root.is_full():
            if root.left:
                self.in_order(root.left)
            print(root.value1, end=' ')
            if root.mid:
                self.in_order(root.mid)
            print(root.value2, end=' ')
            if root.right:
                self.in_order(root.right)
        else:
            if root.left:
                self.in_order(root.left)
            print(root.value1, end=' ')
            if root.right:
                self.in_order(root.right)


# instantiate an AVL tree
tttree = TwoThreeTree()

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
    tttree.insert(element)

# two-three tree
"""
      4
     / \ 
    2   6
   / \ / \ 
  1  3 5  7
"""
print("After insertion:")
tttree.traversal()

# search
key1 = 6; key2 = 8
print("\nSearch: ")

# success
print("search key = %d" % key1)
if tttree.search(key1):
    print("Search successful.")
else:
    print("Search unsuccessful.")

# fail
print("search key = %d" % key2)
if tttree.search(key2):
    print("Search successful.")
else:
    print("Search unsuccessful.")

# deletion
tttree.remove(1)
tttree.remove(7)
tttree.remove(5)
tttree.remove(6)

# After deletion
"""
     3
    / \ 
   2   4
"""

print("After deleting 1, 7, 5, 6:")
tttree.traversal()
