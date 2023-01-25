from math import inf

class Vertex:
    def __init__(self, name = None, parent = None, distance = None):
        self.name = name
        self.parent = parent
        self.distance = distance

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

class Edge:
    def __init__(self, src = None, dst = None, weight = None):
        self.src = src
        self.dst = dst
        self.weight = weight

class Graph:
    def __init__(self, vertices = None, edges = None):
        self.vertices = vertices
        self.edges = edges

    def getNode(self, name):
        for v in self.vertices:
            if v.name == name:
                return v

    def GetInDegrees(self):
        list = []

        for v in self.vertices:
            counter = 0

            for e in self.edges:
                if e.dst == v:
                    counter += 1

            list.append(counter)

        return list

    def GetOutDegrees(self):
        list = []

        for v in self.vertices:
            counter = 0

            for e in self.edges:
                if e.src == v:
                    counter += 1

            list.append(counter)

        return list

    def initialiseSingleSource(self, s):
        for v in self.vertices:
            v.distance = inf
            v.parent = None

        s.distance = 0

    def relax(self, u, v, w):
        if v.distance > u.distance + w:
            v.distance = u.distance + w
            v.parent = u

    def extractMin(self, Q):
        min = Q[0]

        for v in Q:
            if v.distance < min.distance:
                min = v

        Q.remove(min)

        return min

    def getAdj(self, x):
        list = []

        for e in self.edges:
            if e.src == x:
                list.append(e.dst)

        return list

    def getWeight(self, u, v):
        for e in self.edges:
            if e.src == u and e.dst == v:
                return e.weight

    def Dijkstra(self, a):
        self.initialiseSingleSource(a)
        S = []
        Q = self.vertices[:]

        while len(Q) > 0:
            u = self.extractMin(Q)
            S.append(u)
            for v in self.getAdj(u):
                self.relax(u, v, self.getWeight(u, v))

    def printShortestPath(self, a, b, list):
        if a == b:
            list.append(a)
        elif b.parent is not None:
            self.printShortestPath(a, b.parent, list)
            list.append(b)
        else:
            print("There is no such a path")
            list.clear()
            return

    def Bellman_Ford(self, a):
        self.initialiseSingleSource(a)
        for v in self.vertices:
            for e in self.edges:
                self.relax(e.src, e.dst, e.weight)

        for e in self.edges:
            if e.dst.distance > e.src.distance + e.weight:
                return False

        return True

    def ShortestPath(self, a, b, flag):
        list = []

        if(flag == True):
            self.Dijkstra(a)
        else:
            if(self.Bellman_Ford(a)):
                print("Bellman Ford successfully finished")
            else:
                print("Bellman Ford unsuccessfully finished")

        self.printShortestPath(a, b, list)
        return list, b.distance

    def UpdateEdge(self, a, b, w):
        for e in self.edges:
            if e.src == a and e.dst == b:
                e.weight = w
                return

        e = Edge(src = a, dst = b, weight = w)
        self.edges.append(e)

def MakeGraph():
    a = Vertex(name = "a")
    b = Vertex(name = "b")
    c = Vertex(name = "c")
    d = Vertex(name = "d")
    e = Vertex(name = "e")
    f = Vertex(name = "f")
    g = Vertex(name = "g")
    h = Vertex(name = "h")

    vertices = [a, b, c, d, e, f, g, h]

    e1  = Edge(src = a, dst = b, weight = 5 )
    e2  = Edge(src = a, dst = d, weight = 8 )
    e3  = Edge(src = b, dst = d, weight = 9 )
    e4  = Edge(src = d, dst = c, weight = 1 )
    e5  = Edge(src = d, dst = e, weight = 10)
    e6  = Edge(src = d, dst = f, weight = 13)
    e7  = Edge(src = e, dst = g, weight = 7 )
    e8  = Edge(src = f, dst = g, weight = 20)
    e9  = Edge(src = h, dst = c, weight = 16)
    e10 = Edge(src = h, dst = e, weight = 2 )
    e11 = Edge(src = h, dst = g, weight = 24)

    edges = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]

    graph = Graph(vertices = vertices, edges = edges)

    return graph

    #return graph

if __name__ == "__main__":
    #1
    graph = MakeGraph()

    a = graph.getNode("a")
    d = graph.getNode("d")
    g = graph.getNode("g")
    h = graph.getNode("h")

    print("Existing path Demo:")
    list, distance = graph.ShortestPath(a, g, True)
    print("List of nodes on shortest path = {0}".format(list))
    print("Distance = {0}".format(distance))

    print("")

    print("Non existing path Demo:")
    list, distance = graph.ShortestPath(a, h, True)
    print("List of nodes on shortest path = {0}".format(list))
    print("Distance = {0}".format(distance))

    print("")

    print("Update Edge Demo:")
    graph.UpdateEdge(d, g, -4)

    list, distance = graph.ShortestPath(a, g, False)
    print("List of nodes on shortest path = {0}".format(list))
    print("Distance = {0}".format(distance))

    print("")

    print("Update Edge Demo(2):")
    graph.UpdateEdge(a, d, 16)

    list, distance = graph.ShortestPath(a, g, False)
    print("List of nodes on shortest path = {0}".format(list))
    print("Distance = {0}".format(distance))

