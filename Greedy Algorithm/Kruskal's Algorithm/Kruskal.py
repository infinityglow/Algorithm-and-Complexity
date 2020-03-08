"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of Kruskal's algorithm to solve minimum spanning tree
# this algorithm starts sorting the entire edge set in nondecreasing order based on their weight
# then create a forest and each vertex is a separate vertex
# repeat the following steps until the spanning tree is complete(num_processed_edge = |V| - 1):
#   - remove the minimum weighted edge from edge set
#   - if two vertices connected to this edge comes from the separate set,
#   merge them togeter by its rank and the edge can be as the part of spanning tree
#   - otherwise, ignore this edge
# time complexity: Θ(|E|log|E|)

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.parent = self  # point to itself
        self.rank = 0

class Edge(object):
    def __init__(self, pre, next, weight):
        self.pre = pre
        self.next = next
        self.weight = weight

class DisjointSet(object):
    def find(self, v):
        if v.parent is not v:
            return self.find(v.parent)
        return v
    def is_same_set(self, u, v):
        return self.find(u) == self.find(v)
    def union(self, u, v):
        u_rep = self.find(u); v_rep = self.find(v)  # get the representative vertex
        # u_rep's rank is greater than v_rep's rank
        if u_rep.rank > v_rep.rank:
            v_rep.parent = u_rep
            u_rep.rank = max(u_rep.rank, v_rep.rank+1)
        # v_rep's rank is smaller than or equal to u_rep's rank
        else:
            u_rep.parent = v_rep
            v_rep.rank = max(v_rep.rank, u_rep.rank+1)

def Krustal(G):
    V, E = G  # retrieve vertices and edges from G
    E.sort(key=lambda x: x.weight)  # sort edges in nondecreasing order such that e1.w < e2.w < ... < e|E|.w
    total_cost = 0  # initialize total cost to 0
    encounter = 0  # num of processed edges
    d_set = DisjointSet()
    for e in E:
        u = e.pre; v = e.next  # retrieve connecting vertices from an edge
        # whether two vertices are in the same set
        if not d_set.is_same_set(u, v):
            print(u.name + '--' + v.name)
            d_set.union(u, v)
            encounter += 1
            total_cost += e.weight
        else:
            continue
        # spanning tree has completed
        if encounter >= len(V) - 1:
            break
    return total_cost


# instantiate vertices and edges
A = Vertex('A'); B = Vertex('B'); C = Vertex('C'); D = Vertex('D')
E = Vertex('E'); F = Vertex('F'); G = Vertex('G')
E1 = Edge(A, B, 2); E2 = Edge(A, C, 6); E3 = Edge(A, E, 5); E4 = Edge(A, F, 10); E5 = Edge(B, D, 3); E6 = Edge(B, E, 3)
E7 = Edge(C, D, 1); E8 = Edge(C, F, 2); E9 = Edge(D, E, 4); E10 = Edge(D, G, 5); E11 = Edge(F, G, 5)

A.neighbours = [E1, E2, E3, E4]; B.neighbours = [E1, E5, E6]; C.neighbours = [E2, E7, E8]
D.neighbours = [E5, E7, E9, E10]; E.neighbours = [E3, E6, E9]; F.neighbours = [E4, E8, E11]; G.neighbours = [E10, E11]

# stack them together
V_set = [A, B, C, D, E, F, G]
E_set = [E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11]

Graph = [V_set, E_set]

print("Krustal's algorithm:")
print("The minimum spanning tree comprises of the following edges:")
cost = Krustal(Graph)
print("The total cost is %d units" % cost)
