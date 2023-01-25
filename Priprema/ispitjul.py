from enum import Enum
from math import inf
from queue import Queue

class Vertex:
    def __init__(self, c=None, p=None, d=None, f=None, name=None, lastname=None, group=None):
        self.c = c
        self.p = p
        self.d = d
        self.f = f
        self.name = name
        self.lastname = lastname
        self.group = group

    def __str__(self):
        info = "Ime:" + str(self.name) + ", Prezime:" + str(self.lastname) + ", Grupa:" + str(self.group)
        return info

    def __repr__(self):
        info = "Ime:" + str(self.name) + ", Prezime:" + str(self.lastname) + ", Grupa:" + str(self.group)
        return info

class VertexColor(Enum):
    BLACK = 0
    GRAY = 127
    WHITE = 255

class Graph:
    def __init__(self, V=None, E=None):
        self.V = V
        self.E = E
        self.time = 0

    def __str__(self):
        inform = ""
        for source in range(0, len(E)):
            for destination in range(0, len(E[source])):
                edges = str(self.V[source].name) + " -> " + str(self.E[source][destination].name) + "\n"
                inform += edges
        return inform

    def dfs(self):
        dict = {}
        grp = 1
        for u in self.V:
            u.c = VertexColor.WHITE
            u.p = None
        self.time = 0
        for u in self.V:
            if u.c is VertexColor.WHITE:
                list = self.dfs_visit(u)
                for l in list:
                    l.group = grp
                dict[grp] = list
                grp += 1
        return dict

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

if __name__ == "__main__":
    v1 = Vertex(name="Laza", lastname="Lazarevic")
    v2 = Vertex(name="Jovan", lastname="Jovanovic")
    v3 = Vertex(name="Isidora", lastname="Sekulic")
    v4 = Vertex(name="Dragoljub", lastname="Mihajlovic <3")
    v5 = Vertex(name="Borislav", lastname="Pekic")
    v6 = Vertex(name="Ivo", lastname="Andric")
    v7 = Vertex(name="Danica", lastname="Maksimovic")

    V = [v1, v2, v3, v4, v5, v6, v7]
    E = [[v2, v3], [v1], [v1], [v7], [v6], [v5], [v4]]
    G = Graph(V, E)

    print("Testiranje ispisa korisnika:")
    for v in G.V:
        print(v)

    print("")
    print("Testiranje ispisa veza prijateljstava:")
    print(G)
    print("")

    print("Grupe:")
    print(G.dfs())
    print("")

    print("Testiranje ispisa korisnika posle grupisanja:")
    for v in G.V:
        print(v)


