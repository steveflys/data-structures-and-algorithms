
from .stack_queue import Stack_Queue
import pytest


@pytest.fixture
def small_stack_queue():
    s = Stack_Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    return s


@pytest.fixture
def empty_stack_queue():
    e = Stack_Queue()
    return e
