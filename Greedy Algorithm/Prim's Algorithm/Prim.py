"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of Prim's algorithm to solve minimum spanning tree problem
# starting from a picked vertex as source,
# the algorithm builds a min-heap from edges associated with the current vertex by `fix_up`,
# then pop the root element out of the heap as the part of spanning tree and reconstruct heap by `fix_down`.
# after that, we mark the current vertex as `visited`, remove from the `V_set`, and jump to the next vertex,
# if the next one has been `unvisited`, otherwise, execute from the beginning.
# the previous steps are looped until `V_set` is empty
# time complexity: Θ(|E|log|V|)
# space complexity: Θ(|E|+|V|)

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.visited = False

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
def Prim(G, source):
    V, _ = G  # retrieve vertices and edges from G
    v_set = V  # vertices set
    pqueue = []  # priority queue
    source.visited = True; v_set.remove(source); cur = source
    total_cost = 0
    while v_set:
        for e in cur.neighbours:
            if not e.visited:
                e.visited = True
                pqueue.append(e)  # add to the priority queue
                fix_up(pqueue)
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
        print(temp.pre.name + '--' + temp.next.name)
        total_cost += temp.weight
        v_set.remove(cur)
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
source = A

print("Prim's algorithm:")
print("The source vertex is %c" % source.name)
print("The minimum spanning tree comprises of the following edges:")
cost = Prim(Graph, source)
print("The total cost is %d units" % cost)




