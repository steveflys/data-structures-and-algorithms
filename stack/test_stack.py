from .stack import Stack
import pytest


def test_empty_stack_has_no_value(empty_stack):
    assert empty_stack.top is None


def test_insertion(empty_stack):
    assert empty_stack.top is None
    assert empty_stack.push(1).val == 1


def test_empty_val_on_insert(empty_stack):
    with pytest.raises(TypeError) as e:
        empty_stack.push(None)
    # import pdb; pdb.set_trace()
    assert str(e.value) == 'Cannot push a value of none'


def test_push_on_empty_stack(empty_stack):
    empty_stack.push([1, 'Good Boy'])
    assert empty_stack.top.val == [1, 'Good Boy']


def test_peek_on_small_stack(small_stack):
    assert small_stack.peek().val == 3
  

def test_pop_on_small_stack(small_stack):
    assert small_stack.pop().val == 3
    assert small_stack.pop().val == 2