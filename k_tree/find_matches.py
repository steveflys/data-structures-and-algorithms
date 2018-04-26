"""Return the nodes that match the val."""

from .k_tree import KTree


def find_matches(tree, val):
    """Return the nodes that match the val."""
    new = []

    def find(node):
        nonlocal new, val
        if val == node.val:
            new.append(node)

    tree.pre_order(find)

    if new:
        return new
    else:
        return False
