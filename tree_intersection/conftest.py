"""Make test fixtures for testing tree_intersection."""
import pytest
from .bst import BST


@pytest.fixture
def first_bst():
    """Make the first bst."""
    b = BST([20, 17, 21, 18, 22, 19])
    return b


@pytest.fixture
def second_bst():
    """Make the second bst."""
    b = BST([13, 17, 21, 2, 22, 29])
    return b


@pytest.fixture
def third_bst():
    """Make the third bst."""
    b = BST([4, 7, 23, 8, 2, 39])
    return b


@pytest.fixture
def fourth_bst():
    """Make the fourth bst."""
    b = BST(['dog', 'cat', 'fish', 'rat', 'parrot', 'snake'])
    return b


@pytest.fixture
def fifth_bst():
    """Make the fifth bst."""
    b = BST(['dog', 'pet', 'fish', 'gerbil', 'parrot', 'snake'])
    return b
