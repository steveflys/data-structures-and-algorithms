from .node import Node


class Stack:
    def __init__(self, iterable=[]):
        self.top = None
        self._size = 0

        if not isinstance(iterable, (list, dict, tuple)):
            """this checks if the iterable is a true iterable and inserts each value as a new node"""
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
        """remove the node at the top of the stack, decrement the ._size and return the value"""
        val = self.top
        self.top = self.top._next
        self._size -= 1
        return val

    def peek(self):
        """look at the value at the top if the stack"""
        return self.top