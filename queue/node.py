
class Node:

    def __init__(self, val, next=None):

        self.val = val
        self._next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return '{val}'.format(val=self.val)

if __name__=='__main__':