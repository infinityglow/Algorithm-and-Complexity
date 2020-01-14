"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of graph traversal (breadth-first search).

class Vertex(object):
    def __init__(self, value, visited):
        self.value = value
        self.visited = False
        self.neighbours = []  # for storing all adjacent vertices

def display(v):
    print(v.value, end=' ')

def bfs(v):
    v.visited = True
    queue = []  # initialize an empty queue
    queue.append(v)  # enqueue vertex v
    while queue:
        for w in v.neighbours:
            if not w.visited:
                w.visited = True
                queue.append(w)
        v = queue.pop(0)  # dequeue vertex v
        display(v)


# iterate vertices of the graph
def BFS(G):
    V = G.keys()
    for v in V:
        if not v.visited:
            bfs(v)

# instantiate vertices and edges
a = Vertex('a', False)
b = Vertex('b', False)
c = Vertex('c', False)
d = Vertex('d', False)
e = Vertex('e', False)
f = Vertex('f', False)
g = Vertex('g', False)
h = Vertex('h', False)

# instantiate a graph
G = {a: [b, c],
       b: [a, d],
       c: [a, d, f],
       d: [b, c, e],
       e: [d],
       f: [c],
       g: [h],
       h: [g]}

for v, n in G.items():
    v.neighbours.extend(n)

print("The traversal order of the graph for breadth-first search is ")
BFS(G)


