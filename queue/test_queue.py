from .queue import Queue
import pytest


def test_empty_queue_has_no_value(empty_queue):
    assert empty_queue.front is None


def test_enqueue(empty_queue):
    assert empty_queue.back is None
    assert empty_queue.enqueue(1).val == 1


def test_insertion_of_iterable():
    iterable_queue = Queue([1, 2, 3, 4, 5])
    assert iterable_queue.front.val == 1


def test_size_on_small_queue(small_queue):
    assert empty_queue._size == 0
    empty_queue.enqueue(4)
    assert empty_queue._size == 4


# def test_empty_val_on_enqueue(empty_queue):
#     with pytest.raises(TypeError) as e:
#         empty_queue.enqueue(None)
#     assert str(e.value) == 'Cannot enqueue a value of none'


# def test_enqueue_on_empty_queue(empty_queue):
#     empty_queue.enqueue([1, 'Good Boy'])
#     assert empty_queue.top.val == [1, 'Good Boy']


# def test_dequeue_on_small_queue(small_queue):
#     assert small_queue.pop().val == 1
#     assert small_queue.pop().val == 2
#     assert small_queue._size == 1