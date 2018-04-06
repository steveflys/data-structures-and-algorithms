from .node import Node


class BST:

    def __init__(self):

        def __repr__(self):
            return '<BST Root {}>'.format(self)

        def __str__(self):
            return self.root.val

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
