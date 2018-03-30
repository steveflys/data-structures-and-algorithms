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

    
    def insert(self, val):
        """sets the val of the node, sets the next as current head next, sets the node as head"""
        self.head = Node(val, self.head)
        self._size += 1
   

    def find(self, val):
        """searches thru a list for a val """            
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    
    def hasloop(self):
        """ Identify a circular reference in a linked list. Set up a fast and slow linked list crawler and if there is a lopp the fast will catch the slow """
        fast = self.head
        slow = self.head
        speedometer = 1
        while fast:
            fast = current.next
            if fast == slow:
                return True
            if %speedometer == 0:
                slow = current.next
            speedometer += 1
        return False        

if __name__=='__main__':

    ll = LinkedList()
   

