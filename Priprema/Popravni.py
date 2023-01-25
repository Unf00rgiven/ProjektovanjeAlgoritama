class Node:
    def __init__(self, parent=None, data=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data.letter)

class Data:
    def __init__(self, value=None, letter=None):
        self.value = value
        self.letter = letter

    def __str__(self):
        return str(self.letter)

class Tree:
    def __init__(self, root =None):
        self.root = root

    def __str__(self):
        return str(self)

    def insert_node(self, node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.data.value < x.data.value:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data.value < y.data.value:
            y.left = node
        else:
            y.right = node

    def find_min(self, min):
        while min.left is not None:
            min = min.left
        return {min.data.value : min.data.letter}

    def tree_search(self, x, dict , let):
        if x is None or x.data.letter == let:
            return x
        if dict[let] < x.data.value:
            return self.tree_search(x.left, dict, let)
        else:
            return self.tree_search(x.right, dict, let)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def delete_node(self, node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            y = self.find_min(node.right)

            if y.parent != node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y

    def find_word(self, word):
        x = tree.root
        for char in word:
            y = x.left
            z = x.right
            if y is not None and y.data.letter == char:
                x = x.left
            elif z is not None and z.data.letter == char:
                x = x.right
            else:
                return False
        return True


if __name__ == '__main__':
    tree = Tree()

    dict = {"ROOT": 50,
            "E": 25, "P": 75,
            "A": 12, "W": 35, "Y": 55, "R": 80,
            "Q": 7, "S": 30, "I": 45, "T": 65, "M": 100,
            "F": 27, "D": 40, "H": 70,
            "C": 43, "O": 66, "U": 73,
            "N": 67}

    # zadatak a)
    for key in dict:
        tmp = Data(letter=key,value=dict[key])
        tmpNode = Node(data=tmp)
        tree.insert_node(tmpNode)

    # zadatak b)
    print("Pronalazenje minimalnog broja:")
    print(tree.find_min(tree.root))
    print()

    # zadatak c)
    print("Postoji li rec python u recniku?")
    print(tree.find_word("PYTHON"))
    print()

    # zadatak d)
    node_O = tree.tree_search(tree.root, dict, "O")
    tree.delete_node(node_O)

    # Zadatak e)
    print("Postoji li rec python nakon brisanja slova O?")
    print(tree.find_word("PYTHON"))




