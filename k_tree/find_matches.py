"""Return the nodes that match the val."""

from .k_tree import KTree


def find_matches(tree, val):
    """Return the nodes that match the val."""
    new = KTree()

    def find(node):
        nonlocal new, val
        if val == node.val:
            new.insert(node)

    tree.pre_order(find)

    if new.root:
<<<<<<< HEAD
        # import pdb; pdb.set_trace()
=======
>>>>>>> 76feaabc9d995cddfa993cb24fb8e8c5d8896dea
        return new
    else:
        return False
