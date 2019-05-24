from uuid import uuid1
class Node():

    def __init__(self, i, j, current_volume, max_capacity):
        self.i = i
        self.j = j
        self.max_capacity = max_capacity
        self.current_volume = 0
        self.left = None
        self.right = None

        self.edges = set()

    def __str__(self):
        return  str(self.i) + '\,' + str(self.j)# + '|' + str(self.current_volume)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.i, self.j, self.current_volume),
        if self.right:
            self.right.print_tree()

    def get_edges(self, root):
        res = []
        if root:

            if root.left is not None:
                self.edges.add((str(root), str(root.left)))
                self.get_edges(root.left)
            if root.right is not None:
                self.edges.add((str(root), str(root.right)))
                self.get_edges(root.right)
        return res

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.current_volume)
            res = res + self.inorder_traversal(root.right)
        return res

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % str(self)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % str(self)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % str(self)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % str(self)
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


def create_glass_triangle(current_node, existing_left, i, j, max_level):

    if i == max_level:
        return

    if existing_left:
        current_node.left = existing_left
    else:
        current_node.left = Node(i, i-j, 0, 5)
        create_glass_triangle(current_node.left, None, i + 1, j, max_level)
    j += 1

    current_node.right = Node(i, i-j, 0, 5)
    create_glass_triangle(current_node.right, current_node.left.right, i + 1, j, max_level)
    j+=1



root = Node(0, 0, 0, 5)
level = 1
max_level = 5

create_glass_triangle(root, None, 1, 0, max_level)

#print(root.inorder_traversal(root))
root.display()

#a = root.inorder_traversal(root)
#print (a)
root.get_edges(root)
print (root.edges)

import pydot
graph = pydot.Dot(graph_type='graph')

for r in root.edges:
    edge = pydot.Edge(r[0], r[1])
    graph.add_edge(edge)

print (graph)
graph.write('example1_graph.dot')

# from subprocess import check_call
(graph,) = pydot.graph_from_dot_file('example1_graph.dot')
graph.write_png('example1_graph.png')