from .node import Node


class Linked_List:
    def __init__(self, iterable=[]):
        self.head = None
        self._size = 0

    if not isinstance(iterable, (list, dict, tuple)):
        """this checks if the iterable is a true iterable and inserts each value as a new node"""
        raise TypeError('Iterable must be a list, dict, or tuple')   
    for i in iterable:
        self.insert(i)

    def insert(self, val):
        """This will add a node the front of the list"""
        try:
            node = Node(val)
        except TypeError:
            raise TypeError('Cannot insert a value of none')

        node._next = self.head
        self.head = node
        self._size += 1

        return self.head

    def remove(self):
        """remove the node at the head of the linked_list, decrement the ._size and    return the value"""
        val = self.head
        self.head = self.head._next
        self._size -= 1
        return val