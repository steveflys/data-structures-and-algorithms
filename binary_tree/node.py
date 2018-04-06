class Node:

    def __init__(self, val, next=None):

        if val is None:
            raise TypeError('The value cannot be none')

        self.val = val
        self._right = right
        self._left = left

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)
        