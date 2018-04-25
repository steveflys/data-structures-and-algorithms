from .queue import Queue


class Node:

    def __init__(self, val):

        if val is None:
            raise TypeError('The value cannot be none')

        self.val = val
        self.children = []

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class KTree:

    def __init__(self):
        self.root = None

    def __repr__(self):
        return 'KTree root {}'.format(self.root.val)

    def __str__(self):
        return str(self.root.val)

    def pre_order(self, operation):
        def _walk(node=None):
            if node is None:
                return

            operation()
            if len(node.children):
                for child in node.children:
                    _walk(child)

        _walk(self.root)

    def post_order(self, operation):
        def _walk(node=None):
            if node is None:
                return

            if len(node.children):
                for child in node.children:
                    _walk(child)

            operation()

        _walk(self.root)

    def breadth_first(self, operation):
        if self.root is None:
            return False
        queue = [self.root]
        while len(queue):
            node = queue.pop(0)
            for child in node.children:
                queue.append(child)
            operation()

    def insert(self, val, parent=None):
        """inserts new nodes into the tree as a child of the correct node"""
        # import pdb; pdb.set_trace()
        node = Node(val)
        if self.root is None:
            self.root = node
        elif self.root.val == parent:
            self.root.children.append(node)
        elif parent is None:
            # import pdb; pdb.set_trace()
            self.root.children.append(node)
        else:
            def find():
                if node.val == parent:
                    node.children.append(node)
                    return node
            self.breadth_first(find)
           

    def breadth_first_traversal(tree, operation):
        """define function to search nodes in the bredth first order"""
        if tree.root is None:
            return False
        operation()
        qu = Queue()
        if len(self.root.children) > 0:
            for child in self.root.children:
                qu.enqueue(child)
        top = qu.front
        while top:
            node = qu.dequeue
            operation()
            if len(node.children) > 0:
                for child in node.children:
                    qu.enqueue(child)
            top = top.next
