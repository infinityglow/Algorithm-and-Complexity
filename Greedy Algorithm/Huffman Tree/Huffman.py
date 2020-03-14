"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of Huffman tree
# initialize n single-node trees containing symbols of the alphabet given,
# and compute the frequency of each symbol and record it into the node
# create a priority queue for saving nodes
# for each iteration, we pop two nodes with the smallest frequency out of the queue,
# replacing them with a new node whose frequency is the sum of these two
# and set the left child and right child to these two nodes respectively
# the loop is over until a single tree is obtained
# for Huffman code, starting from the Huffman tree's root node,
# the codeword is obtained by searching the symbol leaf node,
# and during the search process, append 0 to the node which is the left child of its parent node
# otherwise, if it is the right child, append 1


class Node(object):
    def __init__ (self, char, freq):
        self.char = char  # character
        self.freq = freq  # frequency
        self.left = None  # left child
        self.right = None  # right child
        self.code = ''  # Huffman code
class Queue(object):
    def __init__ (self):
        self.queue = None  # for saving nodes
        self.length = 0  # length of queue
    def create(self, dict):
        queue = []
        # enqueue
        for char, freq in dict:
            queue.append(Node(char, freq))
        self.queue = queue
        self.length = len(queue)
    def add(self, node):
        # queue is empty
        if self.length == 0:
            self.queue.append(node)
        else:
            # search and insert
            for i in range(self.length):
                if self.queue[i].freq >= node.freq:
                    self.queue.insert(i+1, node)
                    break
            else:
                # node to be inserted is the tail of the queue
                self.queue.insert(self.length, node)
        self.length += 1  # increment queue's length by 1
    def remove(self):
        self.length -= 1  # decrement queue's length by 1
        return self.queue.pop(0)
class HuffmanTree(object):
    def __init__ (self, string):
        self.string = string
        self.char2code = {}  # map from characters to codewords
        self.code2char = {}  # map from codewords to characters
    def compute_freq(self):
        string = self.string
        char_freq = {}
        for char in string:
            char_freq[char] = char_freq.get(char, 0) + 1  # count the frequency of each character
        return sorted(char_freq.items(), key=lambda x:x[1])
    def build(self, queue):
        while queue.length != 1:
            u = queue.remove(); v = queue.remove()
            w = Node(None, u.freq + v.freq)  # create a new node `w` whose `freq` is the sum of u's `freq` and v's `freq`
            w.left = u; w.right = v  # node w points to u and v
            queue.add(w)
        return queue.remove()
    def map(self, root, x=''):
        if root:
            # visit children nodes recursively
            self.map(root.left, x+'0')
            root.code = x
            if root.char:
                self.char2code[root.char] = root.code
                self.code2char[root.code] = root.char
            self.map(root.right, x+'1')
    def encode(self, string):
        code = ''
        for char in string:
            code += self.char2code[char]
        return code
    def decode(self, code):
        string = ''; pattern = ''
        for c in code:
            pattern += c
            # pattern in the dictionary
            if pattern in self.code2char:
                string += self.code2char[pattern]
                pattern = ''
        return string


string = 'ADCEBDABCCADEDBCACBD'
print("The original string is " + string)
ht = HuffmanTree(string)
dic = ht.compute_freq()
print("The frequency of each character: ", dic)
# instantiate an empty priority queue
pq = Queue()
# create a priority queue and construct Huffman tree
pq.create(dic)
root = ht.build(pq)
ht.map(root)
print("Map from character to codeword: ", ht.char2code)
print("Map from codeword to character: ", ht.code2char)
code = ht.encode(string)
print("After encoding: ", code)
print("After decoding: ", ht.decode(code))