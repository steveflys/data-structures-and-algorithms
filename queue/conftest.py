from .queue import Queue
import pytest


@pytest.fixture
def small_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    return q


@pytest.fixture
def empty_queue():
    e = Queue()
    return e
