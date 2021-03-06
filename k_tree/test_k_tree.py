"""Make the tests for the k-ary class."""

import pytest
from .k_tree import KTree
from .print_level_order import print_level_order
from .find_matches import find_matches


def test_insert_first_node():
    """Ensure insert with no root will make the node the root."""
    new_k_tree = KTree()
    new_k_tree.insert(10)
    assert new_k_tree.root.val == 10


def test_insert_with_no_parent():
    """Assert insert with no parent will make the node a child of the root."""
    next_k_tree = KTree()
    next_k_tree.insert(1)
    next_k_tree.insert(10)

    assert next_k_tree.root.children[0].val == 10


def test_post_order(small_k_tree):
    """Verify the node values will come out in the proper post_order sequence."""
    answer = []

    def operation(node):
        answer.append(node.val)
    small_k_tree.post_order(operation)

    assert answer == [5, 6, 7, 2, 8, 3, 4, 1]


def test_pre_order(small_k_tree):
    """Ensure the node values will come out in the proper pre_order sequence."""
    answer = []

    def operation(node):
        answer.append(node.val)

    small_k_tree.pre_order(operation)

    assert answer == [1, 2, 5, 6, 7, 3, 8, 4]


def test_breadth_first(small_k_tree):
    """Make sure the node values will come out in the proper breadth_first sequence."""
    answer = []

    def do_this(node):
        answer.append(node.val)

    small_k_tree.breadth_first(do_this)

    assert answer == [1, 2, 3, 4, 5, 6, 7, 8]


def test_print_level_order(small_k_tree):
    """Test the print level order function on the small K tree."""
    assert print_level_order(small_k_tree) == '1\n234\n5678'


def test_print_level_order_on_empty_tree():
    """Test the print level order function on an empty K tree."""
    tree = KTree()
    tree.insert(10)
    assert print_level_order(tree) == '10\n'


def test_find_matches_with_one_match(small_k_tree):
    """Ensure the find matches will find the matches."""
    answer = find_matches(small_k_tree, 6)

    assert answer.root.val.val == 6
