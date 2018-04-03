from .node import Node
from .stack import Stack


class Stack_Queue:
    def __init__(self):
        self.stack_front = Stack()
        self.stack_front = Stack()
        self._size = 0

    def enqueue(self, val):
        """This will add a node the back of the queue and increment the ._size"""
        try:
            node = Node(val)
        except TypeError:
            raise TypeError('Cannot push a value of none')

        node._next = self.stack_back.top
        self.stack_back.top = node
        self._size += 1

        return self.top

    def dequeue(self):
        """remove the node at the front of the queue, decrement the ._size and return the value"""

        while stack_back.next:
            stack_front.push(stack_back.pop())

        val = stack_back.pop

        while stack_front.next:
            stack_back.push(stack_front.pop())

        return val
