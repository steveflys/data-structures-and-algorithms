from .linked_list import Linked_List as ll
import pytest


def test_empty_linked_list_has_no_value(empty_linked_list):
    """test the val of the empty linked_list is None"""
    assert empty_linked_list.top is None


def test_insertion(empty_linked_list):
    """test that we can push a val into an empty linked_list and increment the ._size of the linked_list"""
    assert empty_linked_list.top is None
    assert empty_linked_list.push(1).val == 1
    assert empty_linked_list._size == 1


def test_instantiate_of_iterable():
    """test if we instantiate a linked_list with an iterable a node will be created for each val in the iterable and the ._size will be updated"""
    iterable_linked_list = linked_list([1, 2, 3, 4, 5])
    assert iterable_linked_list.top.val == 5
    assert iterable_linked_list._size == 5


def test_size_on_empty_linked_list(empty_linked_list):
    """test we can push a new val into an empty linked_list and update the ._size is incremented"""
    assert empty_linked_list._size == 0
    empty_linked_list.push(1)
    assert empty_linked_list._size == 1


def test_empty_val_on_insert(empty_linked_list):
    """test if we try to push a value of None a type erreor will be thrown and rthe correct message will be displayed"""
    with pytest.raises(TypeError) as e:
        empty_linked_list.push(None)
    assert str(e.value) == 'Cannot push a value of none'


def test_push_on_empty_linked_list(empty_linked_list):
    """test we can push a value into the top of the linked_list""" 
    empty_linked_list.push([1, 'Good Boy'])
    assert empty_linked_list.top.val == [1, 'Good Boy']


def test_peek_on_small_linked_list(small_linked_list):
    """test we can return the value of the top of the linked_list with the peek method"""
    assert small_linked_list.peek().val == 3


def test_pop_on_small_linked_list(small_linked_list):
    """test we can remove a node from the top of a linked_list, increment the ._size and return the value"""
    assert small_linked_list.pop().val == 3
    assert small_linked_list.pop().val == 2
    assert small_linked_list._size == 1
