"""Test the tree_intersection function."""

from .tree_intersection import tree_intersection


def test_tree_intersection_with_trees_that_have_matches(first_bst, second_bst):
    """Test tree intersection with trees that have matches."""
    assert tree_intersection(first_bst, second_bst) = {17, 21, 22}


def test_tree_intersection_with_trees_that_have_no_matches(first_bst, third_bst):
    """Test tree intersection with trees that have no matches."""
    assert tree_intersection(first_bst, second_bst) = {}


# def test_tree_intersection_with_trees_that_have_matches(first_bst, second_bst):
#     """Test tree intersection with trees that have matches."""
#     assert tree_intersection(first_bst, second_bst) = {17, 21, 22}


