class Node():
    def __init__(self, data = 0, parent = None, left = None, right = None, balance = 0, height = 0):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.balance = balance
        self.height = height

class Tree():
    #init
    def __init__(self):
        self.root = None

    #adding nodes
    def addNode(self, node):
        if self.root is None:
            self.root = node
            return

        curr = self.root
        pcurr = curr
        while not(curr is None):
            if node.data > curr.data:
                pcurr = curr
                curr = curr.right
                right = True
            else:
                pcurr = curr
                curr = curr.left
                right = False

        node.parent = pcurr
        if right:
            pcurr.right = node
        else:
            pcurr.left = node

    #height calculations
    def height(self, node, h):
        if node is None:
            return 0

        h = max(self.height(node.left, h), self.height(node.right, h)) + 1
        node.height = h-1
        return h

    def calcHeight(self):
        self.height(self.root, 0)

    #balance calculations
    def balance(self, node):
        if (node.left is None) and (node.right is None):
            node.balance = 0
            return
        elif node.left is None:
            node.balance = 0 - node.right.height
            return
        elif node.right is None:
            node.balance = node.left.height
            return

        node.balance = node.left.height - node.right.height
        self.balance(node.left)
        self.balance(node.right)

    def calcBalance(self):
        self.balance(self.root)

    #AVLify
    def rotateR(self, node):
        A = node
        B = node.left

        if B is None:
            return

        if not(A.parent is None):
            if A.parent.right == A:
                A.parent.right = B
            else:
                A.parent.left = B
        else:
            self.root = B

        A.parent = B
        if not(B.right is None):
            A.left = B.right
        else:
            A.left = None
        B.right = A

    def rotateL(self, node):
        A = node
        C = node.right

        if C is None:
            return

        if not (A.parent is None):
            if A.parent.right == A:
                A.parent.right = C
            else:
                A.parent.left = C
        else:
            self.root = C

        A.parent = C
        if not(C.left is None):
            A.right = C.left
        else:
            A.right = None
        C.left = A

    def findIssue(self):
        issues = []

        nodes = []
        curr = self.root
        while not(curr is None) and len(nodes) == 0:
            while not(curr is None):
                nodes.append(curr)
                curr = curr.left
            while curr is None:
                curr = nodes[len(nodes)-1]
                if abs(curr.height) > 1:
                    issues.append(curr)
                curr = curr.right
                if curr is None:
                    nodes.pop()

        if len(issues) == 0:
            return None

        min = issues[0]
        for i in range(1, len(issues)):
            if issues[i].height < min.height:
                min = issues[i]

        return min

    def AVLify(self):
        node = self.findIssue()
        if node is None:
            return

        if node.balance > 0:
            self.rotateR(node)
        else:
            self.rotateL(node)
        self.AVLify()

    #print heights and balance
    def ph(self, node):
        if node is None:
            return
        print(f"{node.data}: {node.height}, {node.balance}")
        self.ph(node.left)
        self.ph(node.right)

    def printHB(self):
        self.ph(self.root)

    #print tree
    def print_tree(self):
        def display(root):
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

#init tree
nodes = [40, 20, 10, 25, 30, 22, 50]
tree = Tree()
root = Node(data=nodes[0])
tree.addNode(root)
for i in range(1, len(nodes)):
    node = Node(data=nodes[i])
    tree.addNode(node)

#calc heights and balance
tree.calcHeight()
tree.calcBalance()

#print tree
tree.print_tree()
print("############")
#tree.printHB()
#print("############")

#AVLify
tree.AVLify()

#print tree
tree.print_tree()
print("############")
#tree.printHB()
#print("############")