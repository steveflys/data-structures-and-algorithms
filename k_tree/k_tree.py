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
        return 'node is {}'.format(str(self.val))


class KTree:

    def __init__(self):
        self.root = None

    def __repr__(self):
        return 'KTree root {}'.format(self.root.val)

    def __str__(self):
        return str(self.root.val)

    def pre_order(self, operation):
        """pre-order traversal of a k-ary tree"""
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            if len(node.children):
                for child in node.children:
                    _walk(child)

        _walk(self.root)

    def post_order(self, operation):
        """post-order traversal of a k-ary tree"""
        def _walk(node=None):
            if node is None:
                return

            if len(node.children):
                for child in node.children:
                    _walk(child)

            operation(node)

        _walk(self.root)

    def breadth_first(self, operation):
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
        """inserts new nodes into the tree as a child of the first parent node"""
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
            def reunion(current):
                if current.val == parent:
                    current.children.append(node)
                    return node

            self.breadth_first(reunion)       

    # def breadth_first_traversal(self, operation):
    #     """define function to search nodes in the bredth first order"""
    #     if tree.root is None:
    #         return False
    #     operation()
    #     qu = Queue()
    #     if len(self.root.children) > 0:
    #         for child in self.root.children:
    #             qu.enqueue(child)
    #     top = qu.front
    #     while top:
    #         node = qu.dequeue
    #         operation()
    #         if len(node.children) > 0:
    #             for child in node.children:
    #                 qu.enqueue(child)
    #         top = top.next
