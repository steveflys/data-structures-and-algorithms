
"""Define the Search Tree Node calss and the Binary Search Tree class."""


class Node:
    """Define the Search Tree Node class."""

    def __init__(self, val):
        """Identify this as a constructor a node."""
        self.val = val
        self.left = None
        self.right = None

        def __repr__(self):
            return('Node val: {}, Right: {}, Left: {}'.format(self.val, self.right.val, self.left.val))

        def __str__(self):
            """Make the str method for the Node."""
            return str(self.val)


class BST:
    """Define the Binary Search Tree class."""

    def __init__(self, iterable=[]):
        """Identify this as a constructor a BST."""
        self.root = None

        if not isinstance(iterable, (list, dict, tuple)):
            """Checks if the iterable is a true iterable and inserts each value as a new node."""
            raise TypeError('Iterable must be a list, dict, or tuple')
        for i in iterable:
            self.insert(i)

    def __repr__(self):
        """Make the repr method for the BST."""
        return 'BST root {}'.format(self.root.val)

    def __str__(self):
        """Make the str method for the BST."""
        return str(self.root.val)

    def insert(self, val):
        """Insert new nodes into the correct side of the tree."""
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
        """Perform an operationon the nodes in the tree in a sorted order."""
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
        """Perform an operationon the nodes in the tree on left tree, then right tree."""
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
        """Perform an operationon the nodes in the tree in a post order."""
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

            operation(node)

        _walk(self.root)
