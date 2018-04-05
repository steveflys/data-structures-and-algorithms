from .node import Node


class Queue:
    def __init__(self, iterable=[]):
        self.front = None
        self.back = None
        self._size = 0

        if not isinstance(iterable, (list, dict, tuple)):
            """ensure the val passed on instantiate is not an iterable a TypeError will be passed"""
            raise TypeError('Iterable must be a list, dict, or tuple')  
        for i in iterable:
            self.enqueue(i)

    def __len__(self):
        return self._size

    def enqueue(self, val):
        """add a value to the back of the queue, increment the size"""
        node = Node(val)
        
        if self._size == 0:
            self.front = node
            self.back = node
        else:
            self.back_next = node._next
 
        self.back._next = node
        self.back = node
        self._size += 1
        return self.back

    def dequeue(self):
        """remove and return the value at the front of the queue"""
        val = self.front
        self.front = self.front._next
        self._size -= 1
        return val
