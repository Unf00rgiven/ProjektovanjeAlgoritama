def getHistogram(array):
    output = []
    freq = {}
    value = []
    for i in array:
        freq[i] = 0
    for i in array:
        freq[i] += 1
    for i in array:
        if i not in value:
            value.append(i)
    for i in value:
        touple = (i, freq[i])
        output.append(touple)
    return output

class Node:
    def __init__(self, parent=None, left=None, right=None, data=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data

class Tree:
    def __init__(self, root=None, nodes=None):
        self.root = root
        self.nodes = nodes

############################################################################################################
    def genTree(self, data):
        histogram = getHistogram(data)
        histogram = sorted(histogram, key=lambda k: k[1])

        nodes = []

        while len(histogram) > 1:
            touple = (histogram[0][0] + histogram[1][0], histogram[0][1] + histogram[1][1])

            nodes.append(Node(data=histogram[0]))
            histogram.remove(histogram[0])

            nodes.append(Node(data=histogram[0]))
            histogram[0] = touple

        nodes.append(Node(data=histogram[0]))

        for i in nodes:
            print(i.data)
        print("#####################################")

        self.root = nodes[len(nodes)-1]
        self.nodes = nodes
        i = 0
        while i+2 < len(nodes):
            nodes[i].parent = nodes[i+2]
            nodes[i+1].parent = nodes[i+2]
            nodes[i+2].left = nodes[i]
            nodes[i+2].right = nodes[i+1]
            i += 2
############################################################################################################
    def findMin(self):
        print(self.nodes[0].data)
############################################################################################################
    def codes(self, value, node):
        if node.data[0] == value:
            return

        if node.left is not None and value in node.left.data[0]:
            print("1", end="")
            self.codes(value, node.left)
        elif  node.right is not None:
            print("0", end="")
            self.codes(value, node.right)

    def printCodes(self, array):
        keys = []
        for i in array:
            if i not in keys:
                keys.append(i)
        for i in keys:
            print(f"Value: {i}, Code:", end="")
            self.codes(i, self.root)
            print()
############################################################################################################
    def pt(self, node):
        if node.left is None and node.right is None:
            print(node.data)
            return
        elif node.right is None:
            print(node.data, node.left.data)
            return
        elif node.left is None:
            print(node.data, node.right.data)
            return

        print(node.data, node.left.data, node.right.data)
        self.pt(node.left)
        self.pt(node.right)

    def print_tree(self):
        self.pt(self.root)
############################################################################################################

input1 = ['a', 'b']
print(input1)

input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
print(input2)

input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
print(input3)

input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
print(input4)

input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']
print(input5)

tree = Tree()
tree.genTree(input5 + 7*['m'])
tree.print_tree()
print("#####################################")
tree.findMin()
print("#####################################")
tree.printCodes(input5 + 7*['m'])