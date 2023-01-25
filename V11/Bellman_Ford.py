from math import inf

class Vertex:   # cvor
    def __init__(self, name):
        self.name = name
        self.p = None   # parent
        self.d = inf    # distance

    def __str__(self):
        return self.name

class Edge:     # ivica
    def __init__(self, src, dst, w):   # putanja od sorce do distenation i w tezina
        self.src = src
        self.dst = dst
        self.w = w

class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E

    def init_single_source(self, s):    # pocetni podesavanje grafa
        for v in self.V:
            v.d = inf
            v.p = None
        s.d = 0

    def get_weight(self, u, v):     # vraca samo za direktrno povezane cvorove
        for e in self.E:
            if e.src == u and e.dst == v:
                return e.w
        return inf

    def relax(self, u, v, w):       # provera da li postoji kraca putanja od cvora do cvora
        if v.d > u.d + w:
            v.d = u.d + w
            v.p = u

    def bellman_ford(self, s):
        self.init_single_source(s)
        for v in self.V:
            for e in self.E:
                self.relax(e.src, e.dst, e.w)
        for e in self.E:            # false ako postoji  negativni ciklus
            if e.dst.d > e.src.d + e.w:
                return False
        return True

    def print_path(self, u, v):
        if v is u:
            print(u)
        elif v.p is None:
            print("No valid path")
        else:
            self.print_path(u, v.p)
            print(v)

if __name__ == "__main__":

    s = Vertex("s")
    t = Vertex("t")
    x = Vertex("x")
    y = Vertex("y")
    z = Vertex("z")

    V = [s, t, x, y, z]

    e1 = Edge(s, t, 6)
    e2 = Edge(s, y, 7)
    e3 = Edge(t, y, 8)
    e4 = Edge(t, z, -4)
    e5 = Edge(t, x, 5)
    e6 = Edge(x, t, -2)
    e7 = Edge(y, x, -3)
    e8 = Edge(y, z, 9)
    e9 = Edge(z, x, 7)
    e10 = Edge(z, s, 2)

    E = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]

    G = Graph(V, E)

    G.bellman_ford(s)
    G.print_path(s, z)
    print(z.d)