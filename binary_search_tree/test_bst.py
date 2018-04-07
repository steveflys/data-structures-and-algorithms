import pytest
from .bst import Node, BST


def test_str_instanciate_with_iterable(backward_bst):
    """test for the proper value at the root for a know iterable insertion"""
    assert str(backward_bst) == '20'


def test_repr_instanciate_with_iterable(backward_bst):
    """test for the proper value at the root for a know iterable insertion"""
    assert repr(backward_bst) == 'BST root 20'


def test_in_order(random_bst):
    """test that values will come out sorted for a random insertion of numbers"""
    answer = []

    def do_this(node):
        answer.append(node.val)

    random_bst.in_order(do_this)

    def sorted_bst(ans):
        i = 0
        x = ans[0]
        for n in ans[1:]:
            if n - x < 0:
                return False
            x = n
        return True
    assert sorted_bst(answer) is True


def test_post_order(backward_bst):
    """this tests the node values will come out in the proper post_order sequence"""
    answer = []

    def do_this(node):
        answer.append(node.val)

    backward_bst.post_order(do_this)

    assert answer == [19, 18, 17, 22, 21, 20]


def test_pre_order(backward_bst):
    """this tests the node values will come out in the proper pre_order sequence"""
    answer = []

    def do_this(node):
        answer.append(node.val)

    backward_bst.pre_order(do_this)

    assert answer == [20, 17, 18, 19, 21, 22]
