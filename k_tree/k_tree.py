"""K-ary tree class and node class for the k-ary tree along with special methods."""


class Node:
    """Node class for a k-ary tree."""

    def __init__(self, val):
        """Make the constructor method for the Node class."""
        if val is None:
            raise TypeError('The value cannot be none')

        self.val = val
        self.children = []

    def __str__(self):
        """Make the str method for the Node."""
        return str(self.val)

    def __repr__(self):
        """Make the repr method for the Node."""
        return 'node is {}'.format(str(self.val))


class KTree:
    """Make the class for a k-ary tree."""

    def __init__(self):
        """Make the constructor method for the KTree class."""
        self.root = None

    def __repr__(self):
        """Make the repr method for the Node."""
        return 'KTree root {}'.format(self.root.val)

    def __str__(self):
        """Make the str method for the Node."""
        return str(self.root.val)

    def pre_order(self, operation):
        """Make a pre-order traversal of a k-ary tree."""
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            if len(node.children):
                for child in node.children:
                    _walk(child)

        _walk(self.root)

    def post_order(self, operation):
        """Make a post-order traversal of a k-ary tree."""
        def _walk(node=None):
            if node is None:
                return

            if len(node.children):
                for child in node.children:
                    _walk(child)

            operation(node)

        _walk(self.root)

    def breadth_first(self, operation):
        """Make a breadth-first traversal of a k-ary tree."""
        def _walk(nodes):
            qu = []
            for node in nodes:
                operation(node)
                for child in node.children:
                    qu.append(child)

            if len(qu):
                _walk(qu)

        if self.root:
            _walk([self.root])

    def insert(self, val, parent=None):
        """Do an insert of new nodes into the tree as a child of the first parent node."""
        node = Node(val)
        if self.root is None:
            self.root = node
        elif self.root.val == parent:
            self.root.children.append(node)
        elif parent is None:
            self.root.children.append(node)
        else:
            def reunion(current):
                if current.val == parent:
                    current.children.append(node)
                    return node

            self.breadth_first(reunion)
