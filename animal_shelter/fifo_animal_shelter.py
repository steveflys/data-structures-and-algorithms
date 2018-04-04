from node import Node
from stack import Stack


class AnimalShelter:
    def __init__(self):
        self.stack_front = Stack()
        self.stack_back = Stack()
        self._size = 0

    def enqueue(self, val):
        """This will add a node the back of the queue and increment the ._size"""
        try:
            node = Node(val)
        except TypeError:
            raise TypeError('Cannot enqueue a value of none')

        node._next = self.stack_back.top
        self.stack_back.top = node
        self._size += 1

        return self.stack_back.top

    def dequeue(self, val):
        """remove the node that has the requested animal nearest to the front of the queue, decrement the ._size and return the value"""

        while self.stack_front.top._next:
            self.stack_back.push(self.stack_front.pop())

        self.stack_back.push(self.stack_front.pop())

        if val is None:
            pet = stack_front.pop()
            while self.stack_front.top._next:
                self.stack_back.push(self.stack_front.pop())

            self.stack_back.push(self.stack_front.pop())

            self._size -= 1

            return pet

        else:
            pet = False

            while self.stack_front.top._next:
                while pet is False:
                    if self.stack_front.top == val:
                        pet = self.stack_front.pop()

                self.stack_back.push(self.stack_front.pop())

            self.stack_back.push(self.stack_front.pop())
        if pet is False:
            print(f'Sorry we do not have any {val}\'s at this time')
        else:
            self._size -= 1
            return pet
