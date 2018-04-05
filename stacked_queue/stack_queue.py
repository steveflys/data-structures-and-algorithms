from .node import Node
from .stack import Stack


class Stack_Queue:
    def __init__(self):
        self.stack_front = Stack()
        self.stack_back = Stack()
        self._size = 0

    def enqueue(self, val):
        """This will add a node the back of the queue and increment the ._size"""
        try:
            node = Node(val)
        except TypeError:
            raise TypeError('Cannot enqueue a value of none')

        node._next = self.stack_back.top
        self.stack_back.top = node
        self._size += 1

        return self.stack_back.top

    def dequeue(self):
        """remove the node at the front of the queue, decrement the ._size and return the value"""

        # import pdb; pdb.set_trace()
        
        while self.stack_back.top._next:
            self.stack_front.push(self.stack_back.pop())

        val = self.stack_back.pop()

        while self.stack_front.top._next:
            self.stack_back.push(self.stack_front.pop())

        self.stack_back.push(self.stack_front.pop())

        self._size -= 1

        return val
