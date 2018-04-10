class Node:

    def __init__(self, val, next=None):

        if val is None:
            raise TypeError('The value cannot be none')

        self.val = val
        self._next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


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

    def enqueue(self, val):
        """add a value to the back of the queue, increment the size"""
        try:
            node = Node(val)
        except TypeError:
            raise TypeError('Cannot enqueue a value of none')

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
