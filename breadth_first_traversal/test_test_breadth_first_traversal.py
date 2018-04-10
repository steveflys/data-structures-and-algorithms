import pytest
from .breadth_first_traversal import breadth_first_traversal


def test_breadth_first_traversal(testing_bst):
    """test that values will come out correctly for a breath first traversal"""
    answer = []

    def do_this(node):
        answer.append(node.val)

    breadth_first_traversal(testing_bst, do_this)
    assert answer == [20, 17, 21, 16, 18, 22]
