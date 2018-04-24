from .queue.queue import queue


class Node:

    def __init__(self, val, children=[]):

        if val is None:
            raise TypeError('The value cannot be none')

        self.val = val
        self.children = children

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class KTree:

    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    def insert(self, parent, val):
        """inserts new nodes into the tree as a child of the correct node"""
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        if parent is None:
            current.children.append(Node)

        def nothing():
            pass

        while current is not parent:
            self.breadth_first(nothing)

        current.children.append(node)

        return node

    def pre_order(self, opertion):
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            for child in node.children:
                _walk(child)

        _walk(self.root)

    def post_order(self, opertion):
        def _walk(node=None):
            if node is None:
                return

            for child in node.children:
                _walk(child)

            operation(node)

        _walk(self.root)

    def breadth_first_traversal(self, operation):
        if self.root is None:
            return False
        queue = [self.root]       
        while len(queue):
            node = queue.pop(0)
            for child in node.children:
                queue.append(child)
            operation(node)
