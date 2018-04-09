from .ll_insertion import Linked_List
import pytest


@pytest.fixture
def small_linked_list():
    s = Linked_List()
    s.insert(1)
    s.insert(2)
    s.insert(3)
    return s


@pytest.fixture
def empty_linked_list():
    e = Linked_List()
    return e


@pytest.fixture
def instanciate_with_iterable():
    i = Linked_List([7, 5, 4, 3, 2, 1])
    return i