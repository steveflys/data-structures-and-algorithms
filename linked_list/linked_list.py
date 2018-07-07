from .node import Node


class Linked_List:
    def __init__(self, iterable=[]):
        self.head = None
        self._size = 0

        if not isinstance(iterable, (list, dict, tuple)):
            """Check if the iterable is a true iterable and inserts each value as a new node."""
            raise TypeError('Iterable must be a list, dict, or tuple')   
        for i in iterable:
            self.insert(i)

    def __repr__(self):
        """Return head and size of linked list when called."""
        return '<head> => {}, <_size> => {}'.format(self.head.val, self._size)

    def __len__(self):
        """Return linked list length when called."""
        return self._size

    def insert(self, val):
        """Add a node the front of the list."""
        try:
            node = Node(val)
        except TypeError:
            raise TypeError('Cannot insert a value of none')

        node._next = self.head
        self.head = node
        self._size += 1

        return self.head

    def remove(self):
        """Remove the node at the head of the linked_list, decrement the ._size and return the value."""
        val = self.head
        self.head = self.head._next
        self._size -= 1
        return val

    def append(self, value):
        """Add a new node to the end of the list."""
        node = Node(value)

        current = self.head
        # import pdb; pdb.set_trace()
        while current._next:
            current = current._next
        current._next = node
        self._size += 1
        return node

    def insert_before(self, new_value, value):
        """Add a new node with the new_value imediately before the first node with the value."""
        try:
            node = Node(new_value)
        except TypeError:
            raise TypeError('Cannot insert a value of none')

        current = self.head

        while current.val != value:
            new_next = current
            current = current._next
        node._next = current
        current = new_next
        current._next = node
        self._size += 1
        return node

    def insert_after(self, new_value, value):
        """Add a new node with the new_value imediately after the first node with the value."""
        try:
            node = Node(new_value)
        except TypeError:
            raise TypeError('Cannot insert a value of none')

        current = self.head

        while current.val != value:
            current = current._next
        node._next = current._next
        current._next = node
        self._size += 1
        return node

    def ll_kth_from_end(self, k):
        """Find node that is (k) from the end."""
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
