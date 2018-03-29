import pytest
from linked_list import LinkedList as LL

@pytest.fixture
def empty_ll():
    return LL()


@pytest.fixture
def small_ll():
    return LL([1, 2, 3, 4])


def test_insert_first_node(empty_ll):
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


import pytest, conftest
from linked_list import LinkedList as LL
from linked_list import merge_lists

def test_empty_ll(empty_ll):
    """
    tests that an empty linked lists head value returns none
    tests that LL with an inserted 1 now has 1 as it's head val
    """
    assert empty_ll.head is None

def test_insert_first_node(empty_ll):
    """
    tests that an empty linked lists head value returns none
    tests that LL with an inserted 1 now has 1 as it's head val
    """
    empty_ll.insert(1)
    assert empty_ll.head.val == 1

def test_make_ll_by_passing_in_iter(small_ll):
    """
    tests that a LL instantiated with an iter returns first val of head as iter
    """
    assert small_ll.head.val == 5

def test_check_valid_iterable():
    """
    check if iterable valid
    """
    with pytest.raises(TypeError) as err:
        LL(2)

    assert str(err.value) == 'Invalid iterable'


def test_inserting_node_after_iter(small_ll):
    """
    tests that a LL instantiated with an iter returns first val of head as iter
    """
    small_ll.insert('new item')
    assert small_ll.head.val == 'new item'
    assert small_ll.head._next.val == 5

# def test_check_insert_not_none(empty_ll):
#     """
#     check if iterable valid
#     """
#     assert empty_ll.insert() == False
#     with pytest.raises(TypeError) as err:
#         empty_ll.insert()

#     assert str(err.value) == 'Must insert a value to use .insert'

def test_find_method_val_at_head_position_valid(small_ll):
    """
    tests that find method returns true when given a val that is in the LL at the head
    """
    assert small_ll.find(5) == True

def test_find_method_val_not_at_head_valid(small_ll):
    """
    tests that find method returns true when given a val that is in the LL but
    not at the first node
    """
    assert small_ll.find(7) == True

def test_find_method_inserted_value_valid(small_ll):
    """
    tests that find method returns true when given a val that has just been inserted
    """
    small_ll.insert('test insert')
    assert small_ll.find('test insert') == True

def test_find_method_val_invalid(small_ll):
    """
    tests that find method returns false when not in the LL
    """
    assert small_ll.find(100) == False

# append

def test_append_linked_list_valid(small_ll):
    """
    tests the append method with an array that already has values
    """
    small_ll.append('hellew')
    assert small_ll.find('hellew') == True

def test_append_empty_linked_list_valid(empty_ll):
    """
    tests the append method with to an array method
    """
    empty_ll.append('hellew')
    assert empty_ll.find('hellew') == True

# insert before

def test_insert_before_with_filled_linked_list_valid(small_ll):
    """
    test that insert before inserts an element correctly
    """
    small_ll.insert_before(7, 'X')
    assert small_ll.head._next._next.val == 'X'

def test_insert_after_with_filled_linked_list_check_size_valid(small_ll):
    """
    test that insert after inserts an element correctly
    """
    assert small_ll.insert_after(7, 'X') == 5
    
def test_insert_after_with_filled_linked_list_valid(small_ll):
    """
    test that insert after inserts an element correctly
    """
    small_ll.insert_after(7, 'X')
    assert small_ll.head._next._next._next.val == 'X'

# kth from end

def test_kth_from_end_valid(small_ll):
    """
    test that method correctly finds the reverse position
    of the element
    """
    assert small_ll.kth_from_end(1).val == 7

def test_kth_from_end_last_el_valid(small_ll):
    """
    test that method correctly finds the reverse position
    of the element
    """
    assert small_ll.kth_from_end(0).val == 8

def test_kth_from_end_invalid(small_ll):
    """
    test that method throws catches exception when passed in value
    is outside of index of list
    """
    with pytest.raises(AttributeError):
        small_ll.kth_from_end(6)

# merge lists function

def test_merge_list_valid(one_four_ll, a_d_ll):
    """
    test merge list function to ensure two lists when passed in are 'zipped' together
    """
    merge_lists(one_four_ll, a_d_ll)
    assert str(one_four_ll.head.val) == 'a'

def test_merge_list_valid_switched(one_four_ll, a_d_ll):
    """
    test merge list function to ensure two lists when passed in are 'zipped' together
    """
    merge_lists(a_d_ll, one_four_ll)
    assert a_d_ll.head._next.val == 'a'
    assert a_d_ll.head.val.val == 1

def test_merge_list_valid_switched_extended(one_four_ll, a_d_ll):
    """
    test merge list function to ensure two lists when passed in are 'zipped' together. traverse further along to check alternation
    """
    merge_lists(a_d_ll, one_four_ll)
    assert a_d_ll.head._next._next._next.val == 'b'

def test_merge_with_one_empty_list(one_four_ll, empty_ll):
    """
    test merge list function with one empty linked list and one full linked list
    """
    merge_lists(one_four_ll, empty_ll)
    assert one_four_ll.head.val == 1
    assert one_four_ll.head._next.val == 2

def test_merge_with_one_empty_list_switched(one_four_ll, empty_ll):
    """
    test merge list function with one empty linked list and one full linked list
    """
    merge_lists(empty_ll, one_four_ll)
    assert one_four_ll.head.val == 1
    assert one_four_ll.head._next.val == 2

def test_merge_with_one_shorter_valid(one_four_ll, a_b_cap_ll):
    """
    test merge list function where second list is shorter
    """
    merge_lists(one_four_ll, a_b_cap_ll)
    # assert one_four_ll.head.val == 1
    assert one_four_ll.head._next._next._next._next.val == 3 