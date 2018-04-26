"""This sets up a the test fuxtures for k-ary trees."""

import pytest
from .k_tree import KTree


@pytest.fixture
def small_k_tree():
    """Make a k-ary tree for pytest."""
    # import pdb; pdb.set_trace()
    k = KTree()
    k.insert(1)
    k.insert(2, 1)
    k.insert(3, 1)
    k.insert(4, 1)
    k.insert(5, 2)
    k.insert(6, 2)
    k.insert(7, 2)
    k.insert(8, 3)
    return k
