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

    def __repr__(self):
        """this will return head and size of linked list when called"""
        return '<head> => {}, <_size> => {}'.format(self.head.val, self._size)

    def __len__(self):
        """returns linked list length when called"""
        return self._size

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

    def ll_kth_from_end(self, k):
        """ find node that is (k) from the end """
        if k < 0 or self._size - k < 0:
            return False
        x = self._size - (k-1)
        node = self.head
        counter = 0
        while node:
            if counter == x:
                return node
            counter += 1
            node = node._next
            return node.val
