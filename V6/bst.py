class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, parent=None, left=None, right=None, data=None):
        """
        Node constructor 
        @param A node data object
        """
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data


class Tree:
    """
    Tree: root
    Methods: insert, inorder_tree_walk, search, search_iterative,
            minimum, maximum, successor, delete, print
    """
    def print_tree(self):
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


node = Node(data=1)
tree = Tree()
tree.print_tree()