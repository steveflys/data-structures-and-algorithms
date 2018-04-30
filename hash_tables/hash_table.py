"""Create a Hash Table class with linked lists as buckets."""
from functools import reduce
from .linked_list.linked import LinkedList


class Hash_Node:
    """Create the node class for a hash_linked_list."""

    def __init__(self, val, key=None, next=None):
        """Identify this as a constructor a hash table Linked List node."""
        if val is None:
            raise TypeError('The value cannot be none')

        self.val = val
        self.key = key
        self._next = next

    def __str__(self):
        """Make the str method for the HashNode."""
        return str(self.val)

    def __repr__(self):
        """Make the repr method for the HashNode."""
        return str(self.val)


class Hash_Linked_List:
    """Create the hash_linked_list class."""

    def __init__(self):
        """Identify this as a constructor a hash table Linked List node."""
        self.head = None
        self._size = 0

    def __repr__(self):
        """Return head and size of linked list when called."""
        return '<head> => {}, <_size> => {}'.format(self.head.val, self._size)

    def __len__(self):
        """Return linked list length when called."""
        return self._size

    def insert(self, val):
        """Add a node the front of the list."""
        try:
            node = Hash_Node(val)
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
    
    def insert_before(self, key, value):
        """add a new node with the new_value imediately before the first node with the value"""
    
        current = self.head

        while current.key != key:
            new_next = current
            current = current._next
        node._next = current
        current = new_next
        current._next = node
        self._size += 1
        return node



class HashTable:
    """Create a Hash Table class with linked lists as buckets."""

    def __init__(self, max_size=1024):
        """Identify this as a constructor for the Hash Table class."""
        self.max_size = max_size
        self.buckets = [None] * self.max_size

    def hash_key(self, key):
        """Make a hash key from a string."""
        if type(key) is not str:
            raise TypeError

        index = 14695981039346656037
        for char in key:
            index = index * 1099511628211
            index = index ^ ord(char)
        index = index % len(self.buckets)
        return index

        self.buckets[index] = LinkedList()

    def get(self, key):
        
        return self.buckets[self.hash_key(key)]

    def remove(self, key):
        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp