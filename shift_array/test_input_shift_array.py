import pytest
from shift_array import insert_shift_array


def test_insert_shift_array_even():
    """ test the insert_shift_array function with an even # of elements"""
    output_array = insert_shift_array([1,2,3,4], 5)
    assert output_array[2] == 5


def test_insert_shift_array_odd():
    """ test the insert_shift_array function with an odd # of elements"""
    output_array = insert_shift_array([4,8,15,23,42], 16)
    assert output_array[3] == 16
