from math import inf

class Vertex:   # cvor
    def __init__(self, name):
        self.name = name
        self.p = None   # parent
        self.d = inf    # distance

    def __str__(self):
        return self.name

    def __repr__(self):     # preklapanje stringa za liste
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

    def __str__(self):
        ret_str = ""
        for e in self.E:
            ret_str += str(e.src) + " -> " + str(e.dst) + ", w = " + str(e.w) + "\n"
        return ret_str

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

    def print_path(self, u, v, ret_list):
        if v is u:
            ret_list.append(u)
        elif v.p is None:
            print("No valid path")
            return None
        else:
            self.print_path(u, v.p, ret_list)
            ret_list.append(v)
        return ret_list

    def shortest_path(self, u, v):
        ret = self.bellman_ford(u)
        if not ret:
            print("No valid path")
        path = self.print_path(u, v, [])
        return path, v.d


    def get_in_degrees(self):   # ulazne linije u cvor
        ret_list = []
        ret_dict = {}
        for v in self.V:
            counter = 0
            for e in self.E:
                if e.dst == v:
                    counter += 1
            ret_list.append(counter)
            ret_dict[v.name] = counter

        return ret_list, ret_dict

    def get_out_degrees(self):   # izlazne linije iz cvora
        ret_list = []
        ret_dict = {}
        for v in self.V:
            counter = 0
            for e in self.E:
                if e.src == v:
                    counter += 1
            ret_list.append(counter)
            ret_dict[v.name] = counter

        return ret_list, ret_dict

    def update_egde(self, u, v, W): # pravimo novu ivicu ili menjamo postojecu
        for e in self.E:
            if e.src == u and e.dst == v:
                e.w = W
                return
        e = Edge(u, v, W)
        E.append(e)


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
    # print(G)
    # print(G.get_in_degrees())
    # print(G.get_out_degrees())
    print(G.shortest_path(s, t))
    G.update_egde(s, x, 3)
    print(G)

