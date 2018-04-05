from .queue import Queue


class Dog:
    def __init__(self):
        self.species = 'dog'


class Cat:
    def __init__(self):
        self.species = 'cat'


class AnimalShelter:
    def __init__(self):
        self.dog_shelter = Queue()
        self.cat_shelter = Queue()
        self.long_queue = Queue()

    def enqueue(self, val):
        """This will add a node the back of the queue and increment the ._size"""
        if val != 'cat' and val != 'dog':
            raise TypeError('Cannot enqueue a value of none')

        if val == 'cat':
            self.cat_shelter.enqueue(Cat())
            self.long_queue.enqueue('c')
        if val == 'dog':
            self.dog_shelter.enqueue(Dog())
            self.long_queue.enqueue('d')
            # import pdb; pdb.set_trace()

    def dequeue(self, pref):
        """remove the node that has the requested animal nearest to the front of the queue, decrement the ._size and return the value"""
        if pref is False:
            pet = self.long_queue.dequeue()
            if pet == 'd':
                pet = self.dog_shelter.dequeue()
                return pet
            else:
                pet = self.cat_shelter.dequeue()
                return pet                
        elif pref == 'dog':
            if not self.dog_shelter:
                return('Sorry we do not have any of those at this time')
            self.long_queue.dequeue()
            pet = self.dog_shelter.dequeue()
            return pet
        elif pref == 'cat':
            if not self.cat_shelter:
                return('Sorry we do not have any of those at this time')
            self.long_queue.dequeue()
            pet = self.cat_shelter.dequeue()
            return pet
        else:
            return('Please choose a dog or cat only')