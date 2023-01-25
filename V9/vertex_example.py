from enum import Enum
from math import inf
from queue import Queue

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, d = None, f = None,  name = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c      # color
        self.p = p      # parent
        self.d = d      # distance/ discovered
        self.f = f      # finished
        self.name = name

    def __str__(self):
        return str(self.name)
	
class VertexColor(Enum):    # nasledjuje klasu enum
        BLACK = 0           # obradjen
        GRAY = 127          # u obradi
        WHITE = 255         # spreman za obradu

class Graph:
    def __init__(self, V = None , E = None):
        self.V = V      # cvorovi grafa
        self.E = E      # ivice grafa
        self.time = 0

    def print_adj(self, u):             # ispis susednih cvorova
        try:
            i = self.V.index(u)
            print(u, " -> [ ", end = "")
            for v in self.E[i]:
                print(v, end = " ")
            print("]")
        except ValueError:
            print("vertex not in graph")

    def bfs(self, s):   # pretraga grafa po sirini
        for u in self.V:
            u.c = VertexColor.WHITE
            u.d = inf
            u.p = None
        s.c = VertexColor.GRAY
        s.d = 0
        s.p = None

        Q = Queue()     # red cekanja
        Q.put(s)        # push u red

        while not Q.empty(): # radi sve dok nije prazan red
            u = Q.get()      # pop iz reda
            for v in self.E[self.V.index(u)]:   # obradjujemo susedne cvorove
                if v.c is VertexColor.WHITE:    # ako nije obradjen do sad
                    v.c = VertexColor.GRAY
                    v.d = u.d + 1
                    v.p = u
                    Q.put(v)
            u.c = VertexColor.BLACK

    def dfs(self): # pretraga grafa u dubinu
        for u in self.V:
            u.c = VertexColor.WHITE
            u.p = None
        self.time = 0;
        for u in self.V:
            if u.c is VertexColor.WHITE:
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.time += 1
        u.d = self.time
        u.c = VertexColor.GRAY
        for v in self.E[self.V.index(u)]:
            if v.c is VertexColor.WHITE:
                v.p = u
                self.dfs_visit(v)
        u.color = VertexColor.BLACK
        self.time += 1
        u.f = self.time


    def print_path(self, s, v): # putanja od s, v
        if v is s:  # ukoliko se poklapaju
            print(s)
        elif v.p is None:   # ako nema roditelja onda nema putanje
            print("no valid path")
        else:
            self.print_path(s, v.p) # nastavljamo dalje
            print(v)



if __name__ == "__main__":
    v1 = Vertex(name = 1)
    v2 = Vertex(name = 2)
    v3 = Vertex(name = 3)
    v4 = Vertex(name = 4)
    v5 = Vertex(name = 5)
    v6 = Vertex(name = 6)

    V_1 = [v1, v2, v3, v4, v5]
    E_1 = [[v2, v5], [v1, v3, v4, v5], [v2, v4], [v2, v3, v5], [v1, v2, v4]]
    G_1 = Graph(V_1, E_1)

    V_2 = [v1, v2, v3, v4, v5, v6]
    E_2 = [[v2, v4], [v5], [v5, v6], [v2], [v4], [v6]]
    G_2 = Graph(V_2, E_2)

    # G_1.print_adj(v1)
    # G_1.print_adj(v2)
    # G_1.print_adj(v3)
    # G_1.print_adj(v4)
    # G_1.print_adj(v5)
    #
    # print()
    #
    # G_2.print_adj(v1)
    # G_2.print_adj(v2)
    # G_2.print_adj(v3)
    # G_2.print_adj(v4)
    # G_2.print_adj(v5)
    # G_2.print_adj(v6)

    #G_1.bfs(v1)
    #G_1.print_path(v1, v4)

    G_2.dfs()
    G_2.print_path(v1, v5)
    print()
    G_2.print_path(v1, v6)