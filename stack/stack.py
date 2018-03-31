from .node import Node


class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        self._size = 0

        if not isinstance(iterable, (list, dict, tuple)):
            raise TypeError('Iterable must be a list, dict, or tuple')   
        for i in iterable:
            self.push(i)

    def push(self, val):
        """This will add a node the top of the stack"""
        try:
            node = Node(val)
        except TypeError:
            raise TypeError('Cannot push a value of none')

        node._next = self.top
        self.top = node
        self._size += 1

        return self.top

    def pop(self):
        val = self.top
        self.top = self.top._next
        return val

    def peek(self):
        return self.top