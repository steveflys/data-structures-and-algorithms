from .bst import Node, BST
from random import randint
import pytest


@pytest.fixture
def testing_bst():
    b = BST([20, 17, 21, 18, 22, 16])
    return b
