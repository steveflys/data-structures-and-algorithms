from .queue import Queue
from .bst import BST


def breadth_first_traversal(bst):
    output = []
    go = Queue()
    current = bst.root
    if current.left:
        go.enqueue(current.left)
    if current.right:
        go.enqueue(current.right)
    x = current.val
    output.append(x)

    while go.front:
        # import pdb; pdb.set_trace()
        current = go.front
        go.dequeue()
        if current.val.left:
            go.enqueue(current.val.left)
        if current.val.right:
            go.enqueue(current.val.right)
        x = current.val.val
        output.append(x)

    return output
