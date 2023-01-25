from enum import Enum	
from math import inf
from queue import Queue


class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c=None, p=None, d=None, name=None):
        """
        Vertex constructor 
        @param c - color
        @param p - parent
        @param d - distance
        @param n - name
        """
        self.c = c
        self.p = p
        self.d = d
        self.name = name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
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
        self.time = 0

    """
    Print adjacent of u
    """
    def print_adj(self, u):
        print(u, '-> [ ', end="")
        for v in self.E[self.V.index(u)]:
            print(v, end=" ")
        print(']')

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
            print(v)

    def top_dfs(self):
        L = []
        for u in self.V:
            u.c = VertexColor.WHITE
            u.p = None

        self.time = 0
        for u in self.V:
            if u.c is VertexColor.WHITE:
                L.insert(0, self.dfs_visit(u))

        return L

    def dfs_visit(self, u):
        L = []
        self.time = self.time + 1
        u.d = self.time
        u.c = VertexColor.GRAY

        for v in self.E[self.V.index(u)]:
            if v.c is VertexColor.WHITE:
                v.p = u
                L.insert(0, self.dfs_visit(v))

        u.c = VertexColor.BLACK
        self.time = self.time + 1
        u.f = self.time
        L.insert(0, u)

        return L


class VertexColor(Enum):
    BLACK = 0
    GRAY = 127
    WHITE = 255


if __name__ == "__main__":
    under = Vertex(name='undershorts')
    pants = Vertex(name='pants')
    belt = Vertex(name='belt')
    shirt = Vertex(name='shirt')
    tie = Vertex(name='tie')
    jacket = Vertex(name='jacket')
    socks = Vertex(name='socks')
    shoes = Vertex(name='shoes')
    watch = Vertex(name='watch')

    #          1               2            3         4          5       6      7     8   9
    E = [[pants, shoes], [belt, shoes], [jacket], [belt, tie], [jacket], [], [shoes], [], []]
    V = [under, pants, belt, shirt, tie, jacket, socks, shoes, watch]

    G = Graph(V, E)
    L = G.top_dfs()
    print(L)
