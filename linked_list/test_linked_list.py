from .linked_list import Linked_List
import pytest


def test_empty_linked_list_has_no_value(empty_linked_list):
    """test the val of the empty linked_list is None"""
    assert empty_linked_list.head is None


def test_insertion(empty_linked_list):
    """test that we can push a val into an empty linked_list and increment the ._size of the linked_list"""
    assert empty_linked_list.head is None
    assert empty_linked_list.insert(1).val == 1
    assert len(empty_linked_list) == 1


def test_instantiate_of_iterable():
    """test if we instantiate a linked_list with an iterable a node will be created for each val in the iterable and the ._size will be updated"""
    iterable_linked_list = Linked_List([1, 2, 3, 4, 5])
    assert iterable_linked_list.head.val == 5
    assert len(iterable_linked_list) == 5
    assert repr(iterable_linked_list) == '<head> => 5, <_size> => 5'


def test_empty_val_on_insert(empty_linked_list):
    """test if we try to push a value of None a type erreor will be thrown and the correct message will be displayed"""
    with pytest.raises(TypeError) as e:
        empty_linked_list.insert(None)
    assert str(e.value) == 'Cannot insert a value of none'


def test_remove_on_small_linked_list(small_linked_list):
    """test we can remove a node from the head of a linked_list, decrement the ._size and return the value"""
    assert small_linked_list.remove().val == 3
    assert small_linked_list.remove().val == 2
    assert len(small_linked_list) == 1


def test_ll_kth_from_end_on_empty_ll(empty_linked_list):
    assert empty_linked_list.ll_kth_from_end(2) is False


def test_ll_kth_from_end_with_k_too_big(small_linked_list):
    assert small_linked_list.ll_kth_from_end(4) is False


def test_ll_kth_from_end_on_small_ll(small_linked_list):
    assert small_linked_list.ll_kth_from_end(2) == 2
