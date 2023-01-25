from enum import Enum
from math import inf
from queue import Queue


class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, p=None, d=None, name=None):
        """
        Vertex constructor
        @param p - parent
        @param d - distance
        @param n - name
        """
        self.p = p
        self.d = d
        self.name = name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class Edge:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, src=None, dst=None, w=None):
        """
        Edge constructor
        @param src - source vertex
        @param dst - destination vertex
        @param w - edge weight
        """
        self.src = src
        self.dst = dst
        self.w = w

    def __str__(self):
        return str(self.name)


class Graph:
    def __init__(self, V=None, E=None):
        """
        Graph constructor
        @param V - list of vertexes
        @param E - list of edges
        """
        self.V = V
        self.E = E

    """
    Print path from vertex s to vertex v
    """
    def print_path(self, s, v):
        if v is s:
            print(s)
        elif v.p is None:
            print("No path from", s, "to", v, "exists.")
        else:
            self.print_path(s, v.p)
            print(v, "-------- Predjena kilometraza:", v.d)

    def get_adj(self, v):
        ret = []
        for e in self.E:
            if v == e.src:
                ret.append(e.dst)

        return ret

    def get_weight(self, s, d):
        for e in self.E:
            if e.src == s and e.dst == d:
                return e.w

        return -1

    def extract_min(self, Q):
        minV = Q[0]
        for v in Q:
            if v.d < minV.d:
                minV = v

        Q.remove(minV)

        return minV

    def relax(self, u, v, w):
        if v.d > u.d + w:
            v.d = u.d + w
            v.p = u

    def initialize_single_source(self, s):
        for v in G.V:
            v.d = inf
            v.p = None

        s.d = 0

    def dijkstra(self, s):
        self.initialize_single_source(s)
        S = []
        Q = G.V[:]
        while len(Q) > 0:
            u = self.extract_min(Q)
            S.append(u)
            for v in self.get_adj(u):
                self.relax(u, v, self.get_weight(u, v))


if __name__ == "__main__":
    v1 = Vertex(name='Novi Sad')
    v2 = Vertex(name='Naplatna NS')
    v3 = Vertex(name='Petrovaradin')
    v4 = Vertex(name='Ruma')
    v5 = Vertex(name='Naplatna SP')
    v6 = Vertex(name='Stara Pazova')
    v7 = Vertex(name='Sremski Karlovci')
    v8 = Vertex(name='Pecinci')
    v9 = Vertex(name='NP Simanovci')
    v10 = Vertex(name='Iskljucenje Batajnica')
    v11 = Vertex(name='Batajnica')
    v12 = Vertex(name='Ukljucenje na AP E70')
    v13 = Vertex(name='Beograd')

    V = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13]

    e1 = Edge(v1, v2, 9)
    e2 = Edge(v1, v3, 7)
    e3 = Edge(v1, v7, 14)
    e4 = Edge(v1, v4, 33)
    e5 = Edge(v2, v5, 45)
    e6 = Edge(v3, v7, 6)
    e7 = Edge(v4, v8, 16)
    e8 = Edge(v5, v10, 28)
    e9 = Edge(v6, v11, 13)
    e10 = Edge(v6, v5, 5)
    e11 = Edge(v6, v9, 14)
    e12 = Edge(v7, v6, 32)
    e13 = Edge(v8, v9, 15)
    e14 = Edge(v9, v12, 11)
    e15 = Edge(v10, v11, 4)
    e16 = Edge(v10, v12, 16)
    e17 = Edge(v11, v13, 22)
    e18 = Edge(v12, v13, 20)

    E = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18]

    G = Graph(V, E)
    G.dijkstra(v1)
    G.print_path(v1, v13)
    print('Ukupna duzina je: ', v13.d)
