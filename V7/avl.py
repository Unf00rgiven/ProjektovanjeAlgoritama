class Node:  # klasa za pravljenje elementa stabla
    def __init__(self, p=None, l=None, r=None, d=None):
        self.parent = p
        self.left = l
        self.right = r
        self.data = d
        self.height = 0         # visina
        self.bf = 0             # bilans faktor

    def __str__(self):  # redefinise print da moze da isprinta polje klasa
        str = f"Node: {self.data}"      # printa sva polja od jednom
        if self.parent:
            str += f', parent: {self.parent.data}'
        if self.left:
            str += f', left: {self.left.data}'
        if self.right:
            str += f', right: {self.right.data}'
        str += f', height: {self.height}'
        str += f', bilans factor: {self.bf}'

        return str


class Tree:  # klasa za pravljenje stabla
    def __init__(self, r=None):
        self.root = r

    def insert(self, z):  # dodavanje elementa u stablo
        y = None  # x je "tmp"
        x = self.root

        while x is not None:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z

        self.calculate_height(tree.root)    # racuna visine nakon svakog dodavanja
        self.bilans_factor(tree.root)       # racuna bilans nakon svakog dodavanja

    def print_tree(self):  # funkcija za printanje stabla
        def display(root):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if root.right is None and root.left is None:
                line = '%s' % root.data
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if root.right is None:
                lines, n, p, x = display(root.left)
                s = '%s' % root.data
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if root.left is None:
                lines, n, p, x = display(root.right)
                s = '%s' % root.data
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(root.left)
            right, m, q, y = display(root.right)
            s = '%s' % root.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(self.root)
        for line in lines:
            print(line)

    def in_order_tree_walk(self, x):  # ispis elemenata u sortiranom nizu
        if x is not None:
            self.in_order_tree_walk(x.left)
            print(x)
            self.in_order_tree_walk(x.right)

    def tree_search(self, x, value):  # trazi po stablu value koji je u nasem slucaju int
        if x is None or x.data == value:
            return x
        if value < x.data:
            return self.tree_search(x.left, value)
        else:
            return self.tree_search(x.right, value)

    def tree_search_iter(self, x, value):  # iterativni search
        while x is not None and value != x.data:
            if value < x.data:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self, x):  # idemo do skroz levog elemetna
        if x.left is None:
            return x
        else:
            return self.minimum(x.left)

    def maximum(self, x):  # idemo do skroz desnog elementa
        if x.right is None:
            return x
        else:
            return self.maximum(x.right)

    def successor(self, x):  # kad bi niz bio sortiran, vraca sledeci element posle x
        if x.right is not None:
            return self.minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def trasplant(self, u, v):  # koristicemo u fuknciji za brisanje elemenata iz stabla
        if u.parent is None:  # menjamo u i v u stablu pre brisanja
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, z):  # brisemo element iz stabla
        if z.left is None:
            self.trasplant(z, z.rigth)
        elif z.right is None:
            self.trasplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.trasplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.trasplant(z, y)
            y.left = z.left
            y.left.parent = y

    def calculate_height(self, x):
        if x is not None:             # prolazi kroz celo stablo
            hl = self.calculate_height(x.left)
            hr = self.calculate_height(x.right)
            x.height = max(hl, hr) + 1
            return x.height
        else:
            return -1

    def bilans_factor(self, x):
        if x is not None:       # prolazi kroz celo stablo
            self.bilans_factor(x.left)
            self.bilans_factor(x.right)
            x.bf = self.calculate_height(x.left) - self.calculate_height(x.right)
    #        if (abs(x.bf) > 1):
    #            rotation(x)

    # 1def rotation(self, x):
    #     if(x.bf > 1):
    #
    #     if(x.bf < -1):
    #


if __name__ == "__main__":
    node = Node(d=16)


    array = [50, 37, 82, 26, 42, 70, 90, 31, 71, 100]
    tree = Tree()
    for el in array:
        tree.insert(Node(d=el))

    tree.print_tree()
    tree.in_order_tree_walk(tree.root)


