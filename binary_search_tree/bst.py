
class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

        def __repr__(self):
            return('Node val: {}, Right: {}, Left: {}'.format(self.val, self.right.val, self.left.val))

        def __str__(self):
            return str(self.val)


class BST:
    def __init__(self):
        self.root = None

        if not isinstance(iterable, (list, dict, tuple)):
            """this checks if the iterable is a true iterable and inserts each value as a new node"""
            raise TypeError('Iterable must be a list, dict, or tuple')
        for i in iterable:
            self.insert(i)

    def __repr__(self):
        return 'BST root {}'.format(self.root.val)

    def __str__(self):
        return str(self.root.val)

    def insert(self, val):
        """inserts new nodes into the correct side of the tree""" 
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break

            if val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break

        return node

    def in_order(self, operation):
        """does an operation on the nodes in the tree in a sorted order"""
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            operation(node)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, operation):
        """does an operation on the nodes in the tree when passing the left side by traversing the left tree, then right tree"""
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, operation):
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

            operation(node)

        _walk(self.root)
