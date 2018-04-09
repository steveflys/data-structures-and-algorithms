from .ll_insertion import Linked_List
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


def test_append_on_small_linked_list(small_linked_list):
    """test the .append by adding a new value at the end of a linked_list and verifing the ._size is updated and the new node is at the end"""
    small_linked_list.append(4)
    assert repr(small_linked_list) == '<head> => 3, <_size> => 4'
    current = small_linked_list.head
    contents = []
    for i in list(range(4)):
        # import pdb; pdb.set_trace()
        contents.append(current.val)
        current = current._next
    assert contents == [3, 2, 1, 4]


def test_insert_before_on_small_linked_list(instanciate_with_iterable):
    """test the .insert_before by adding a new value into a known linked_list and verifing the ._size is updated and the new node is where it is suposed to be"""
    instanciate_with_iterable.insert_before(6, 7)
    assert repr(instanciate_with_iterable) == '<head> => 1, <_size> => 7'
    current = instanciate_with_iterable.head
    contents = []
    for i in list(range(7)):
        # import pdb; pdb.set_trace()
        contents.append(current.val)
        current = current._next
    assert contents == [1, 2, 3, 4, 5, 6, 7]


def test_insert_after_on_small_linked_list(instanciate_with_iterable):
    """test the .insert_after by adding a new value into a known linked_list and verifing the ._size is updated and the new node is where it is suposed to be"""
    instanciate_with_iterable.insert_after(6, 5)
    assert repr(instanciate_with_iterable) == '<head> => 1, <_size> => 7'
    current = instanciate_with_iterable.head
    contents = []
    for i in list(range(7)):
        # import pdb; pdb.set_trace()
        contents.append(current.val)
        current = current._next
    assert contents == [1, 2, 3, 4, 5, 6, 7]
