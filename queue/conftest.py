from .queue import Queue
import pytest


@pytest.fixture
def small_queue():
    """create a queue with 3 values"""
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    return q


@pytest.fixture
def empty_queue():
    """cfreate an empty queue"""
    e = Queue()
    return e
