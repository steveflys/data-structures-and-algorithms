from .queue import Queue
from .bst import BST


def breadth_first_traversal(bst, operation):

    go = Queue()
    node = bst.root
    import pdb; pdb.set_trace()
    if node.left.val:
        go.enqueue(node.left.val)
    if node.right.val:
        go.enqueue(node.right.val)
    operation

    while go:
        node.next = go.front.val
        node = node.next
        go.dequeue
        if node.left.val:
            go.enqueue(node.left.val)
        if node.right.val:
            go.enqueue(node.right.val)
        operation

    operation
