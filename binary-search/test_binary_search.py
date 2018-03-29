import pytest
from binary_search import binary_search as bs

def test_binary_search_with():
    """Test for a value that exists"""
    assert bs([4,8,15,16,23,42], 15) == 2

def test_binary_search_without():
    """Test for a value that exists"""
    assert bs([11,22,33,44,55,66,77], 90) == -1

