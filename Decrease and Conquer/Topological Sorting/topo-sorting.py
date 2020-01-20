"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of topological sorting (Kahn algorithm)
# step:
# 1. find the source vertex, i.e., in-degree is equal to 0
# 2. remove the vertex associated with its edge(s)
# 3. repeat step 1 and 2 until no such vertex in the graph

class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.visited = False

def find_source(G):
    source = None
    V = G.keys(); E = G.values()  # unpack G
    for v in V:
        for neighbour in E:
            for vertex in neighbour:
                # check each edges
                if vertex is v:
                    break
            else:
                continue
            break
        else:
            source = v
            break
    return source

def topo_main(G):
    order = []
    while len(G) != 0:
        s = find_source(G)
        if s is None:
            return "No such topological order."
        order.append(s.value)
        G.pop(s)
    return order


a = Vertex('advanced mathematics')
b = Vertex('linear algebra')
c = Vertex('probability theory')
d = Vertex('data structure')
e = Vertex('machine learning')
f = Vertex('computer vision')

G = {a: [b, e],
       b: [c, e],
       c: [e],
       d: [e],
       e: [f],
       f: []}

print(topo_main(G))


