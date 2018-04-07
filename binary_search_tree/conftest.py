from .bst import Node, BST
from random import randint
import pytest


@pytest.fixture
def random_bst():
    values = [randint(0, 50) for p in range(9)]
    r = BST(values)
    return r


@pytest.fixture
def backward_bst():
    b = BST([20, 17, 21, 18, 22, 19])
    return b
