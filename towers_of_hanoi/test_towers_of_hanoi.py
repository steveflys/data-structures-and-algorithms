from . import towers_of_hanoi
from .stack import Stack
import pytest


def test_if_peg_a_loads_correctly():
    i = list(range(1, 3 + 1))
    i.reverse()
    peg_a = Stack(i)
    peg_b = Stack()
    peg_c = Stack()
    assert peg_a.pop().val == 1
    assert peg_a.pop().val == 2
    assert peg_a.pop().val == 3
    assert peg_a.peek() is None


def test_if_even_number_completes():
    towers_of_hanoi.towers_of_hanoi(4)
    assert towers_of_hanoi.a is None
    assert towers_of_hanoi.b is None
    assert towers_of_hanoi.c == 1
   

def test_if_even_number_completes():
    towers_of_hanoi.towers_of_hanoi(3)
    towers_of_hanoi.towers_of_hanoi(4)
    assert towers_of_hanoi.a is None
    assert towers_of_hanoi.b is None
    assert towers_of_hanoi.c == 1

