from .queue import Queue
from .bst import BST


def breadth_first_traversal(bst, operation):

    go = Queue()
    current = bst.root
    if current.left:
        go.enqueue(current.left)
    if current.right:
        go.enqueue(current.right)
    x = current.val
    operation()

    while go.front:
        current = go.front
        go.dequeue()
        if current.val.left:
            go.enqueue(current.val.left)
        if current.val.right:
            go.enqueue(current.val.right)
        x = current.val.val
        # import pdb; pdb.set_trace()
        operation()

    operation
