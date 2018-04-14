import pytest
from largest_product_array import largest_product as lp


def test_with_integers():
    """Test for the value of a 2D array"""
    assert lp([[1, 2], [3, 4], [5, 6], [7, 8]]) == 56
    

def test_with_negative_numbers():
    assert lp([[1, 2], [3, 4], [-8, 6], [5, -7]]) == 24


def test_with_floatss():
    assert lp([[1, 2], [3, 4.7], [8, 6], [5, 7.5]]) == 48

