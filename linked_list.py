from node import Node as Node


class LinkedList:
    
    """This is the Single Linked List class and all it's magic methods"""
    def __init__(self, iter=[]):
        self._current = None
        self.head = None
        self._length = 0
        self.iter = iter
    
    """Insert a iterable item"""
        for item in reversed(self.iter):
            self.insert(item)
   
    """returns the value of the head and size of the list"""
    def __repr__(self):
        return '<head> => {}, <_size> => {}'.format(self.head.val, self._length.val)
    
    """Returns the length of the list"""
    def __len__(self):
        return self._length

    """sets the val of the node, sets the next as current head next, sets the node as head"""
    def insert(self, val):
        self.head = Node(val, self.head)
        self._size += 1
    """
    searches thru a list for a val
    """    
    def find(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

if __name__=='__main__':

    ll = LinkedList()
   