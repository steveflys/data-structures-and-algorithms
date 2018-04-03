from .stack_queue import Stack_Queue
import pytest

def test_insertion(empty_stack_queue):
    """test that we can push a val into an empty stack-queue and increment the ._size of the stack_queue"""
    empty_stack.enqueue(1).val == 1
    assert empty_stack_queue._size == 1


def test_empty_val_on_insert(empty_stack_queue):
    """test if we try to push a value of None a type erreor will be thrown and the correct message will be displayed"""
    with pytest.raises(TypeError) as e:
        empty_stack.push(None)
    assert str(e.value) == 'Cannot enqueue a value of none'


def test_enqueue_on_small_stack_queue(small_stack_queue):
    """test we can push a value into the back of the stack_queue""" 
    empty_stack.push([1, 'Good Boy'])
    assert empty_stack_queue == [1, 'Good Boy']


def test_dequeue_on_small_stack_queue(small_stack_queue):
    """test we can remove a node from the front of a stack_queue, decrement the ._size and return the value"""
    assert small_stack_queue.dequeue() == 1
    assert small_stack_queue.dequeue() == 2
    assert small_stack_queue._size == 1