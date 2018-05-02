"""Make function that will return the values found both of 2 BSTs."""
from .bst import BST


def tree_intersection(bst_1, bst_2):
    """Make a function that will return the values found both of 2 BSTs."""
    first_search = set()
    matches = set()

    def first(node):
        first_search.add(node.val)

    bst_1.in_order(first)

    def intersects(node):
        """Insert the current node value if it is in the other bst."""
        if node.val in first_search:
            matches.add(node.val)

    bst_2.in_order(intersects)

    if matches == set():
        return None
    else:
        return matches
