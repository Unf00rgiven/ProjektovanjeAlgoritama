from enum import Enum
from math import inf
from queue import Queue


class Vertex:

    def __init__(self, c=None, p=None, d=None, f=None ,name=None):
        self.c = c
        self.p = p
        self.d = d
        self.f = f
        self.name = name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class Graph:
    def __init__(self, V=None, E=None):

        self.V = V
        self.E = E
        self.time = 0

    def print_adj(self, u):
        print(u, '-> [ ', end="")
        for v in self.E[self.V.index(u)]:
            print(v, end=" ")
        print(']')

    def print_path(self, s, v):
        if v is s:
            print(s)
        elif v.p is None:
            print("No path from", s, "to", v, "exists.")
        else:
            self.print_path(s, v.p)
            print(v)

    def bfs(self, s):
        for u in self.V:
            if u is not s:
                u.c = VertexColor.WHITE
                u.d = inf
                u.p = None

        s.c = VertexColor.GRAY
        s.d = 0
        s.p = None

        Q = Queue()
        Q.put(s)

        while not Q.empty():
            u = Q.get()
            for v in self.E[self.V.index(u)]:
                if v.c is VertexColor.WHITE:
                    v.c = VertexColor.GRAY
                    v.d = u.d + 1
                    v.p = u
                    Q.put(v)

            u.c = VertexColor.BLACK

    def top_dfs(self):          # isto kao DFS samo sto ima povratnu listu od poslednjeg koji je pronadjen ondosno 
        L = []                  # prvog koji treba da se izvrsi
        for u in self.V:
            u.c = VertexColor.WHITE
            u.p = None

        self.time = 0
        for u in self.V:
            if u.c is VertexColor.WHITE:
                L = self.dfs_visit(u) + L

        return L

    def dfs_visit(self, u):
        L = []
        self.time = self.time + 1
        u.d = self.time
        u.c = VertexColor.GRAY

        for v in self.E[self.V.index(u)]:
            if v.c is VertexColor.WHITE:
                v.p = u
                L = self.dfs_visit(v) + L

        u.c = VertexColor.BLACK
        self.time = self.time + 1
        u.f = self.time
        L = [u] + L
        return L


class VertexColor(Enum):
    BLACK = 0
    GRAY = 127
    WHITE = 255

if __name__ == "__main__":
    # list1 = [4, 5]
    # list2 = [1, 2]
    #
    # print(list1 + list2)
    # print(list2 + list1)
    # print("-------------------------------------\n")

    under = Vertex(name="undershorts")
    pants = Vertex(name="pants")
    belt = Vertex(name="belt")
    shirt = Vertex(name="shirt")
    tie = Vertex(name="tie")
    jacket = Vertex(name="jacket")
    socks = Vertex(name="socks")
    shoes = Vertex(name="shoes")
    watch = Vertex(name="watch")

    V = [under, pants, belt, shirt, tie, jacket, socks, shoes, watch]
    E = [[pants, shoes], [belt, shoes], [jacket], [belt, tie], [jacket], [], [shoes], [], []]

    G = Graph(V, E)
    top_list = G.top_dfs()
    for v in top_list:
        print(v)
    print(top_list)
