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
        # import pdb; pdb.set_trace()
        return new
    else:
        return False
