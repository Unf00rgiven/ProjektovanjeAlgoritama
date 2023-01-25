from enum import Enum
from math import inf
from queue import Queue


class Vertex:

    def __init__(self, p=None, d=None, name=None):
        self.p = p
        self.d = d
        self.name = name


    def __str__(self):
        return str(self.name)


class Edge:
    def __init__(self, src=None, dst=None, w=None):
        self.src = src
        self.dst = dst
        self.w = w

class Graph:
    def __init__(self, V=None, E=None):
        self.V = V
        self.E = E

    def __str__(self):
        var = ""
        for e in self.E:
            var += str(e.src) + " cvor -> " + str(e.dst) + ", w = " + str(e.w) + "\n"
        return var

    def ShortestPath(self, s, v):
        self.dijkstra(s)
        self.print_path(s, v)

    def print_path(self, s, v):
        if v is s:
            print("Do cvora", s, "presli smo:", s.d)
        elif v.p is None:
            print("Nema putanje od ", s, "do ", v)
        else:
            self.print_path(s, v.p)
            print("Do cvora", v, "presli smo:", v.d)

    def get_adj(self, v):
        ret = []

        for e in self.E:
            if v == e.src:
                ret.append(e.dst)

        return ret

    def extract_min(self, Q):
        local_min = Q[0]
        for v in Q:
            if v.d < local_min.d:
                local_min = v
        Q.remove(local_min)
        return local_min


    def initialize_single_source(self, s):
        for v in self.V:
            v.d = inf
            v.p = None
        s.d = 0

    def get_weight(self, s, d):
        for e in self.E:
            if e.src == s and e.dst == d:
                return e.w
        return -1

    def relax(self, u, v, w):
        if v.d > u.d + w:
            v.d = u.d + w
            v.p = u

    def dijkstra(self, s):
        self.initialize_single_source(s)
        S = []
        Q = self.V[:]
        while len(Q) > 0:
            u = self.extract_min(Q)
            S.append(u)
            for v in self.get_adj(u):
                self.relax(u, v, self.get_weight(u, v))

if __name__ == "__main__":
    v1 = Vertex(name="A")
    v2 = Vertex(name="B")
    v3 = Vertex(name="C")
    v4 = Vertex(name="D")
    v5 = Vertex(name="E")
    v6 = Vertex(name="F")

    V = [v1, v2, v3, v4, v5, v6]

    e1 = Edge(v1, v2, 5)
    e2 = Edge(v1, v5, 23)
    e3 = Edge(v2, v3, 3)
    e4 = Edge(v2, v5, 7)
    e5 = Edge(v3, v4, 6)
    e6 = Edge(v3, v6, 13)
    e7 = Edge(v4, v5, 11)
    e8 = Edge(v5, v6, 2)

    E = [e1, e2, e3, e4, e5, e6, e7, e8]

    G = Graph(V, E)
    print(G)

    G.ShortestPath(v1, v6)
    G.ShortestPath(v6, v4)



