from math import inf
from enum import Enum

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """

    def __init__(self, p=None, d=None, name=None):
        """
        Vertex constructor
        @param color, parent, auxilary data1, auxilary data2
        """
        self.p = p
        self.d = d
        self.name = name

    def __str__(self):
        return str(self.name)


class Graph:
    def __init__(self, V = None, E = None):
        self.V = V
        self.E = E

    def __str__(self):
        ret_str = ""
        for e in self.E:
            ret_str += str(e.src) + " -> " + str(e.dst) + " , w = " + str(e.w) + "\n"
        return ret_str

    def ShortestPath(self, nodeA, nodeB):
        self.dijkstra(nodeA)
        lista = self.print_path(nodeA, nodeB, [])
        print('Shortest path:')
        for v in lista:
            print(v)
        print('Duzina: ', nodeB.d)

    def getAdj(self, v):
        ret = []
        for e in self.E:
            if v == e.src:
                ret.append(e.dst)
        return ret

    def getWeight(self, s, d):
        for e in self.E:
            if e.src == s and e.dst == d:
                return e.w
        return -1

    def relax(self, u, v, w):
        if v.d > u.d + w:
            v.d = u.d + w
            v.p = u

    def initSingleSrc(self, s):
        for v in self.V:
            v.d = inf
            v.p = None
        s.d = 0

    def extractMin(self, Q):
        minV = Q[0]
        for v in Q:
            if v.d < minV.d:
                minV = v
        return minV

    def dijkstra(self, s):
        self.initSingleSrc(s)
        S = []
        Q = self.V[:]

        while len(Q) > 0:
            u = self.extractMin(Q)
            Q.remove(u)
            S.append(u)
            for v in self.getAdj(u):
                self.relax(u, v, self.getWeight(u, v))

    def print_path(self, s, v, lista):
        if v is s:
            lista.append(s)
        elif v.p is None:
            print('No path from', s, 'to', v)
            return None, None
        else:
            lista = self.print_path(s, v.p, lista)
            lista.append(v)
        return lista


class Edge:
    def __init__(self, src = None, dst = None, w = None):
        self.src = src
        self.dst = dst
        self.w = w


vA = Vertex(name = 'A')
vB = Vertex(name = 'B')
vC = Vertex(name = 'C')
vD = Vertex(name = 'D')
vE = Vertex(name = 'E')
vF = Vertex(name = 'F')

ab = Edge(src = vA, dst = vB, w = -6)
ad = Edge(src = vA, dst = vD, w = -4)
ae = Edge(src = vA, dst = vE, w = 15)
bc = Edge(src = vB, dst = vC, w = 7)
cf = Edge(src = vC, dst = vF, w = -3)
de = Edge(src = vD, dst = vE, w = 11)
ec = Edge(src = vE, dst = vC, w = 13)
fe = Edge(src = vF, dst = vE, w = 5)

G = Graph([vA, vB, vC, vD, vE, vF], [ab, ad, ae, bc, cf, de, ec, fe])
print(G)
G.ShortestPath(vA, vE)




