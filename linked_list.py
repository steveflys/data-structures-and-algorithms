from node import Node


class LinkedList:
    """
    This is the Single Linked List class and all it's magic methods
    """
    def __init__(self, iter=[]):
        self._current = None
        self.head = None
        self._length = 0
    """
    Insert a iterable item
    """
        for item in reversed(iter):
            self.insert(item)

    def __repr__(self):
        # Assuming head will have a val (You need to handle the case of None)
        return '<head> => {}'.format(self.head.val)

    def __len__(self):
        return self._length

    def insert(self, val):
    """
       3 steps to insert to front of linked list
        set val: node = Node(val)
        set next: node.next = self.head
        set as head: self.head = node
    """
        self.head = Node(val, self.head)
        self._size += 1
    
    def find(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False        