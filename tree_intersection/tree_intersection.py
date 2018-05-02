"""Make function that will return the values found both of 2 BSTs."""
from ..hash_tables.hash_table import HashTable, HashNode, HashLinkedList
from ..binary_search_tree.bst import BST


def tree_intersection(bst_1, bst_2):
    """Make a function that will return the values found both of 2 BSTs."""
    first_search = set()
    matches = set()
    bst_1.pre_order(first_search.add(current.val))

    def intersects(current.val):
        """Insert the current node value if it is in the other bst"""
        if current.val in first_search:
            intersects.add(current.val)

    bst_2.pre_order(intersects)

    return intersects
