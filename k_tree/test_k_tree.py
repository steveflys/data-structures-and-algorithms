import pytest
from .k_tree import KTree


def test_insert_with_no_parent(small_k_tree):
    """test insert with no parent will make the node a child of the root"""
    small_k_tree.insert(4, 10)
    assert small_k_tree.root.children = [2, 3, 4, 10]


def test_post_order(small_k_tree):
    """this tests the node values will come out in the proper post_order sequence"""
    answer = []

    def do_this(node):
        answer.append(node.val)

    small_k_tree.post_order(do_this)

    assert answer == [1, 2, 5, 6, 7, 3, 8, 9, 4]


def test_pre_order(small_k_tree):
    """this tests the node values will come out in the proper pre_order sequence"""
    answer = []

    def do_this(node):
        answer.append(node.val)

    small_k_tree.pre_order(do_this)

    assert answer == [5, 8, 7, 2, 8, 9, 3, 4, 1]


def test_breadth_first(small_k_tree):
    """this tests the node values will come out in the proper breadth_first sequence"""
    answer = []

    def do_this(node):
        answer.append(node.val)

    small_k_tree.pre_order(do_this)

    assert answer == [1, 2, 3, 4, 5, 6, 7, 8, 9]
