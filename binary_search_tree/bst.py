
class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

        def __repr__(self):
            return('Node val: {}, Right: {}, Left: {}'.format(self.val, self.right.val, self.left.val))

        def __str__(self):
            return self.val


class BST:
    def __init__(self, iterable=[]):
        self.root = None

        def __repr__(self):
            return '<BST Root {}>'.format(self.root.val)

        def __str__(self):
            return self.root.val

        if not isinstance(iterable, (list, dict, tuple)):
            """this checks if the iterable is a true iterable and inserts each value as a new node"""
            raise TypeError('Iterable must be a list, dict, or tuple')   
        for i in iterable:
            self.insert(i)

        def insert(self, val):
            node = Node(val)
            current = self.root

            if self.root is None:
                self.root = node
                return node

            while current:
                if val >= current.val:
                    if current.right is not None
                        current = current.right
                    else:
                        current.right = node
                        break

                if val < current.val:
                    if current.left is not None
                        current = current.left
                    else:
                        current.left = node
                        break

            return leaf       

        def in_order(self, operation):
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
            def _walk(node=None):
                if node is None:
                    return

                operation(node)

                if node.left is not None:
                    _walk(node.left)

                if node.right is not None:
                    _walk(node_right)

            _walk(self.root)

        def post_order(self, operation):
            def _walk(node=None):
                if node is None:
                    return

                if node.left is not None:
                    _walk(node.left)

                if node.right is not None:
                    _walk(node_right)

                operation(node)

            _walk(self.root)


