"""This sets up a the test fuxtures for k-ary trees."""

import pytest
from .k_tree import KTree


@pytest.fixture
def small_k_tree():
    """Make a k-ary tree for pytest."""
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


@pytest.fixture
def small_k_tree():
    """Make a second k-ary tree for pytest."""
    r = KTree()
    r.insert(1)
    r.insert(2, 1)
    r.insert(3, 1)
    r.insert(3, 1)
    r.insert(5, 2)
    r.insert(6, 2)
    r.insert(3, 2)
    r.insert(8, 3)
    return r
