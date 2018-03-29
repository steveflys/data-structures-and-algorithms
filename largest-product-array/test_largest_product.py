import pytest
from largest_product_array import largest_product as lp

def test_largest_product():
    """Test for the value of a 2D array"""
    assert lp([ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ], [ 7, 8 ] ]) == 56
    assert lp([ [ 1, 2 ], [ 3, 4 ], [ 8, 5 ], [ 6, 7 ] ]) == 48
    assert lp([ [ 1, 2 ], [ 3, 4 ], [ -8, 6 ], [ 5, -7 ] ]) == 24