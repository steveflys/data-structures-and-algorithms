import pytest
from .k_tree import KTree


@pytest.fixture
def small_k_tree():
    k = KTree()
    k.insert(8, 1)
    k.insert(1, 2)
    k.insert(1, 3)
    k.insert(1, 4)
    k.insert(2, 5)
    k.insert(2, 6)
    k.insert(2, 7)
    k.insert(3, 8)
    k.insert(3, 9)
    return k
