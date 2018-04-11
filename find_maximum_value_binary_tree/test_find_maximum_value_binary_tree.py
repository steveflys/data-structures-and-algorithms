from .find_maximum_value_binary_tree import find_maximum_value_binary_tree
from .bst import BST
import pytest


def test_with_bst():
    """test for the proper value a know binary tree"""
    test_bst = BST([20, 17, 21, 18, 22, 19])
    assert find_maximum_value_binary_tree(test_bst) == 22


def test_with_bst_with_negative_numbers():
    """test for the proper value a know binary tree"""
    test_bst = BST([20, 17, 21, 18, -22, 19, 0])
    assert find_maximum_value_binary_tree(test_bst) == 21


def test_with_empty_bst():
    """test for the knsertion of an empty binary tree"""
    test_bst = BST()
    assert find_maximum_value_binary_tree(test_bst) is 0

