from .stack import Stack
import pytest


def test_empty_stack_has_no_value(empty_stack):
    """test the val of the empty stack is None"""
    assert empty_stack.top is None


def test_insertion(empty_stack):
    """test that we can push a val into an empty stack and increment the ._size of the stack"""
    assert empty_stack.top is None
    assert empty_stack.push(1).val == 1
    assert empty_stack._size == 1


def test_instantiate_of_iterable():
    """test if we instantiate a stack with an iterable a node will be created for each val in the iterable and the ._size will be updated"""
    iterable_stack = Stack([1, 2, 3, 4, 5])
    assert iterable_stack.top.val == 5
    assert iterable_stack._size == 5


def test_size_on_empty_stack(empty_stack):
    """test we can push a new val into an empty stack and update the ._size is incremented"""
    assert empty_stack._size == 0
    empty_stack.push(1)
    assert empty_stack._size == 1


def test_empty_val_on_insert(empty_stack):
    """test if we try to push a value of None a type erreor will be thrown and rthe correct message will be displayed"""
    with pytest.raises(TypeError) as e:
        empty_stack.push(None)
    assert str(e.value) == 'Cannot push a value of none'


def test_push_on_empty_stack(empty_stack):
    """test we can push a value into the top of the stack""" 
    empty_stack.push([1, 'Good Boy'])
    assert empty_stack.top.val == [1, 'Good Boy']


def test_peek_on_small_stack(small_stack):
    """test we can return the value of the top of the stack with the peek method"""
    assert small_stack.peek().val == 3


def test_pop_on_small_stack(small_stack):
    """test we can remove a node from the top of a stack, increment the ._size and return the value"""
    assert small_stack.pop().val == 3
    assert small_stack.pop().val == 2
    assert small_stack._size == 1
