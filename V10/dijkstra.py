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

    def __repr__(self):
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

    def print_path(self, s, v):
        if v is s:
            print(s)
        elif v.p is None:
            print("No path from", s, "to", v, "exists.")
        else:
            self.print_path(s, v.p)
            print(v, " do ove tacke presli smo:", v.d)

    def get_adj(self, v):       # pronalazenje suseda
        ret = []

        for e in self.E:
            if v == e.src:
                ret.append(e.dst)

        return ret

    def extract_min(self, Q):   # dobijamo minimum distancu iz cvorova
        local_min = Q[0]
        for v in Q:
            if v.d < local_min.d:
                local_min = v
        Q.remove(local_min)
        return local_min


    def initialize_single_source(self, s):  # pocetno podesavanje algoritma dijkstra
        for v in self.V:
            v.d = inf
            v.p = None
        s.d = 0

    def get_weight(self, s, d):     # tezina/duzina veze izmedju cvorova s i d
        for e in self.E:
            if e.src == s and e.dst == d:
                return e.w
        return -1

    def relax(self, u, v, w):   # smanjuje/relaksira tezine ivica izmedju cvorova 
        if v.d > u.d + w:
            v.d = u.d + w
            v.p = u

    def dijkstra(self, s):
        self.initialize_single_source(s)
        S = []
        Q = self.V[:] # test [] + self.V
        while len(Q) > 0:
            u = self.extract_min(Q)
            S.append(u)
            for v in self.get_adj(u):
                self.relax(u, v, self.get_weight(u, v))

if __name__ == "__main__":
    v1 = Vertex(name="Novi Sad")
    v2 = Vertex(name="Naplatna rampa NS")
    v3 = Vertex(name="Petrovaradin")
    v4 = Vertex(name="Sremski Karlovci")
    v5 = Vertex(name="Ruma")
    v6 = Vertex(name="Naplatna rampa Stara Pazova")
    v7 = Vertex(name="Stara Pazova")
    v8 = Vertex(name="Pecinci")
    v9 = Vertex(name="Naplatna rampa Simanovci")
    v10 = Vertex(name="Iskljucenje Batajnica")
    v11 = Vertex(name="Batajnica")
    v12 = Vertex(name="Ukljucenje na AP E70")
    v13 = Vertex(name="Beograd")

    V = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13]

    e1 = Edge(v1, v2, 9)
    e2 = Edge(v1, v3, 7)
    e3 = Edge(v1, v4, 14)
    e4 = Edge(v1, v5, 33)
    e5 = Edge(v2, v6, 45)
    e6 = Edge(v3, v4, 6)
    e7 = Edge(v5, v8, 16)
    e8 = Edge(v2, v6, 45)
    e9 = Edge(v4, v7, 32)
    e10 = Edge(v8, v9, 15)
    e11 = Edge(v7, v9, 14)
    e12 = Edge(v6, v10, 28)
    e13 = Edge(v7, v11, 13)
    e14 = Edge(v9, v12, 11)
    e15 = Edge(v10, v11, 4)
    e16 = Edge(v10, v12, 16)
    e17 = Edge(v11, v13, 22)
    e18 = Edge(v12, v13, 20)


    E = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18]

    G = Graph(V, E)
    G.dijkstra(v1)
    G.print_path(v1, v13)
