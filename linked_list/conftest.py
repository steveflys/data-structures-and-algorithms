from .linked_list import Linked_List
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