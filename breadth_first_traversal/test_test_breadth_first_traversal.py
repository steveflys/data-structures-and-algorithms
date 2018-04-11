import pytest
from .breadth_first_traversal import breadth_first_traversal


def test_breadth_first_traversal(testing_bst):
    """test that values will come out correctly for a breath first traversal"""

    # def do_this(current):
    #     answer.append(current.val.val)

    assert breadth_first_traversal(testing_bst) == [20, 17, 21, 16, 18, 22]
