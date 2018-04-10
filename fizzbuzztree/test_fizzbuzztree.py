import pytest
from .bst import BST
from .fizzbuzztree import fizz_buzz_tree


def test_fizz_buzz_tree():
    val = [1, 3, 4, 5, 6, 8, 9, 15, 19, 25, 27, 30, 60]

    fbb = BST(val)
    
    fizz_buzz_tree(fbb)
    
    answer = []

    def do_this(node):
        answer.append(node.val)

    fbb.in_order(do_this)

    assert answer == [1, 'Fizz', 4, 'Buzz', 'Fizz', 8, 'Fizz', 'FizzBuzz', 19, 'Buzz', 'Fizz', 'FizzBuzz', 'FizzBuzz']
