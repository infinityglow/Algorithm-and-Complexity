"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of Dijkstra's algorithm to solve single-source shortest path problem
# for each vertex, it has two domains, one is for saving the previous vertex, and another
# one is for saving the minimal distance from the source node.
# The algorithm starts picking a source, and set distance value to zero, while others to infinity
# mark the source node as `visited`. For each `unvisited` edges neighbouring the current vertex,
# add them into a min-heap, then `fix_up`, and update adjacent vertex's `min_distance` and `parent`
# based on the formula: min(v, u+edge(u, v)),
# where u is the current vertex, and v is the corresponding adjacent vertex
# pop up the root element from the heap before `fix_down` and if both connecting vertices are not `visited`,
# we assign the `unvisited` vertex as current vertex
# iterate the above steps until `V_set` is empty

from math import inf

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.visited = False
        self.parent = None
        self.min_dis = inf

class Edge(object):
    def __init__(self, pre, next, weight):
        self.pre = pre
        self.next = next
        self.visited = False
        self.weight = weight

def fix_up(queue):
    temp_idx = len(queue) - 1
    parent_idx = (temp_idx - 1) // 2
    heap = False
    while not heap and parent_idx >= 0:
        # swap elements if heap property is violated
        if queue[temp_idx].weight < queue[parent_idx].weight:
            queue[temp_idx], queue[parent_idx] = queue[parent_idx], queue[temp_idx]
        else:
            heap = True
        # update indices
        temp_idx = parent_idx
        parent_idx = (temp_idx - 1) // 2
def fix_down(queue):
    temp_idx = 0; size = len(queue)
    temp_ver = queue[temp_idx]  # save vertex temporarily
    heap = False
    while not heap and 2 * temp_idx + 1 < size:
        j = 2 * temp_idx + 1  # index of left child
        # right child exists
        if j < size - 1:
            # compare two children's weight
            if queue[j].weight > queue[j + 1].weight:
                j = j + 1
        # whether violate heap property or not
        if queue[j].weight >= temp_ver.weight:
            heap = True
        else:
            queue[temp_idx] = queue[j]
            temp_idx = j  # update temp_idx
    queue[temp_idx] = temp_ver
def get_next_ver(u, e):
    if e.pre is u:
        return e.next
    return e.pre
def Dijkstra(G, source):
    V, _ = G  # retrieve vertices and edges from G
    v_set = V  # vertices set
    pqueue = []  # priority queue
    source.visited = True; v_set.remove(source)
    cur = source; cur.min_dis = 0  # initialize source's min distance to 0
    while v_set:
        for e in cur.neighbours:
            if not e.visited:
                e.visited = True
                pqueue.append(e)  # add to the priority queue
                fix_up(pqueue)
                temp = get_next_ver(cur, e)
                if cur.min_dis + e.weight < temp.min_dis:
                    temp.min_dis = cur.min_dis + e.weight
                    temp.parent = cur
        pqueue[0], pqueue[-1] = pqueue[-1], pqueue[0]
        temp = pqueue.pop()  # get rid of the root element
        fix_down(pqueue)
        if not temp.pre.visited:
            cur = temp.pre
        elif not temp.next.visited:
            cur = temp.next
        else:
            continue  # the next vertex has been visited
        cur.visited = True
        v_set.remove(cur)
def get_shortest_path(v):
    path=[]
    while v is not None:
        path.insert(0, v.name)
        v = v.parent
    return path


# instantiate vertices and edges
A = Vertex('A'); B = Vertex('B'); C = Vertex('C')
D = Vertex('D'); E = Vertex('E'); F = Vertex('F')
E1 = Edge(A, B, 7); E2 = Edge(A, E, 1); E3 = Edge(A, F, 6); E4 = Edge(B, C, 2)
E5 = Edge(B, D, 4); E6 = Edge(C, D, 9); E7 = Edge(C, E, 3); E8 = Edge(E, F, 3)

A.neighbours = [E1, E2, E3]; B.neighbours = [E1, E4, E5]; C.neighbours = [E4, E6, E7]
D.neighbours = [E5, E6]; E.neighbours = [E2, E7, E8]; F.neighbours = [E3, E8]

# stack them together
V_set = [A, B, C, D, E, F]
E_set = [E1, E2, E3, E4, E5, E6, E7, E8]

Graph = [V_set, E_set]
source = A
targets = [C, D, F]

print("Dijkstra's algorithm:")
Dijkstra(Graph, source)
print("The source vertex is %c" % source.name)
for target in targets:
    print("The shortest path from %c to %c is: " % (source.name, target.name))
    path = get_shortest_path(target)
    for v in path[:-1]:
        print(v, end='->')
    print(path[-1])
    print("The minimal distance is %d" % target.min_dis)