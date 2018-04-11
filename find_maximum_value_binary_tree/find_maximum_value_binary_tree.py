
def find_maximum_value(bst):
    """traverses all on the nodes in the tree and compares the values to find the maximum value"""

    x = 0

    def _walk(node=None):
        nonlocal x
        if node is None:
            return x

        if node.val > x:
            x = node.val

        if node.left is not None:
            _walk(node.left)

        if node.right is not None:
            _walk(node.right)

    _walk(bst.root)

    return x
