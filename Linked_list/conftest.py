from .stack import Stack
import pytest


@pytest.fixture
def small_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    return s


@pytest.fixture
def empty_stack():
    e = Stack()
    return e
