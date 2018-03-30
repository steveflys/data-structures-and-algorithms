from node import Node

class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        # self.-size = 0 (optional)

    def push(self, val):
        """ What is this"""

        try:
            node = Node(val)
        except TypeError:
            #handle the thing
            pass

        node._next = self.top
        self.top = node       

        return self.top

    def pop(self):
        pass

    def peek(self):
        pass