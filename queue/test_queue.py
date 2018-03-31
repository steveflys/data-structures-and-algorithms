from .queue import Queue
import pytest


def test_empty_queue_has_no_value(empty_queue):
    """Test if an empty queue has no nodes or value"""
    assert empty_queue.front is None


def test_enqueue(empty_queue):
    """test if we can add a new node ot the back of the queue"""
    assert empty_queue.back is None
    assert empty_queue.enqueue(1).val == 1


def test_insertion_of_iterable():
    """test if we can instantiate a new queue with an iterable and a new node will be made for every value in the iterable"""
    iterable_queue = Queue([1, 2, 3, 4, 5])
    assert iterable_queue.front.val == 1
    assert iterable_queue._size == 5


def test_for_valid_iterable():
    """test if we try to pass anything other than an instantiate a new Queue an error will be thrown"""
    with pytest.raises(TypeError) as e:
        iterable_queue = Queue('cat')
    assert str(e.value) == 'Iterable must be a list, dict, or tuple'


def test_size_on_small_queue(empty_queue):
    assert empty_queue._size == 0
    empty_queue.enqueue(4)
    assert empty_queue._size == 1


def test_empty_val_on_enqueue(empty_queue):
    with pytest.raises(TypeError) as e:
        empty_queue.enqueue(None)
    assert str(e.value) == 'Cannot enqueue a value of none'


def test_enqueue_on_empty_queue(empty_queue):
    empty_queue.enqueue([1, 'Good Boy'])
    assert empty_queue.back.val == [1, 'Good Boy']


def test_dequeue_on_small_queue(small_queue):
    assert small_queue.dequeue().val == 1
    assert small_queue.dequeue().val == 2
    assert small_queue._size == 1