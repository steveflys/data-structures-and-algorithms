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

    def __str__(self):
        return str(self.root.val)

    def __repr__(self):
        return str(self.root.val)

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

    def breadth_first(self, operation):
        if self.root is None:
            return False
        queue = [self.root]
        while len(queue):
            node = queue.pop(0)
            for child in node.children:
                queue.append(child)
            operation(node)

    def insert(self, val, parent=None):
        """inserts new nodes into the tree as a child of the correct node"""
        node = Node(val)
        if self.root is None:
            self.root = node
        elif self.root.val == parent:
            self.root.children.append(node)
        elif parent is None:
            self.root.children.append(node)
    
        current = self.root

        qu = Queue()
        if len(current.children) > 0:
            for child in current.children:
                qu.enqueue(child)
        top = qu.front
        while top:
            import pdb; pdb.set_trace()
            current = qu.dequeue.val
            if current.val == parent:
                current.children.append(node)
                break
            if len(current.children) > 0:
                for child in current.children:
                    qu.enqueue(child)
            top = top.next
        

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
