"""Create a Hash Table class with linked lists as buckets."""


class HashNode:
    """Create the node class for a hash_linked_list."""

    def __init__(self, key, val, next=None):
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


class HashLinkedList:
    """Create the hash_linked_list class."""

    def __init__(self):
        """Identify this as a constructor a hash table Linked List node."""
        self.head = None
        self._size = 0

    def __repr__(self):
        """Return head and size of linked list when called."""
        return '<head> => {}, <_size> => {}'.format(self.head.val if self.head else None, self._size)

    def __len__(self):
        """Return linked list length when called."""
        return self._size

    def insert(self, key, val):
        """Insert a new value into the bucket at ther head of the list."""
        try:
            node = HashNode(key, val)
        except TypeError:
            raise TypeError('Cannot insert a value of none')

        node._next = self.head
        self.head = node
        self._size += 1


class HashTable:
    """Create a Hash Table class with linked lists as buckets."""

    def __init__(self, max_size=1024):
        """Identify this as a constructor for the Hash Table class."""
        self.max_size = max_size
        self.buckets = [HashLinkedList() for _ in range(self.max_size)]

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

    def set(self, key, val):
        """Insert a new value at the given key."""
        index = self.hash_key(key)
        self.buckets[index].insert(key, val)

    def get(self, key):
        """Get the value(s) at the key."""
        index = self.hash_key(key)
        # import pdb; pdb.set_trace()
        value = []
        if self.buckets[index]._size > 0:
            current = self.buckets[index].head
            while current._next:
                if current.key == key:
                    value.append(current.val)
                current = current._next
            if current.key == key:
                    value.append(current.val)
            return value
        else:
            return None

    def remove(self, key):
        """Remove the nodes from the bucket at the key and return the value(s)."""
        index = self.hash_key(key)
        value = []
        if self.buckets[index]._size > 0:
            current = self.buckets[index].head
            if self.buckets[index].head.key == key:
                value.append(current.val)
                self.buckets[index].head = current._next
                current = current._next
            while current._next:
                # import pdb; pdb.set_trace()
                last = current
                if current.key == key:
                    value.append(current.val)
                    new_next = current._next
                    current.val = None
                    current._next = None
                    current.key = None
                    current = last
                    current._next = new_next
                current = current._next
            if current.key == key:
                    value.append(current.val)
                    current.val = None
                    current._next = None
                    current.key = None
            return value
        else:
            return None
