from linked_list import LinkedList as LL
from node import Node as Node

def hasloop(self):
    counter = 1
    current = self.head
    while current.next:
        current = current.next
        counter += 1
        if counter > self._length:
            return True
    return False        