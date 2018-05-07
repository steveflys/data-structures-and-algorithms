"""Made tersts for the sort functions."""

from .merge import merge_sort
from .selection import selection_sort


def test_merge_sort_on_integers():
    """Test the merge sort on integers."""
    assert merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93]


def test_merge_sort_on_words():
    """Test the merge sort on words."""
    assert merge_sort(['cat', 'dog', 'snake', 'gerbil']) == ['cat', 'dog', 'gerbil', 'snake']


def test_merge_sort_with_neg():
    """Test the merge sort on integers with neg integer."""
    assert merge_sort([54, 26, 93, 17, 77, 31, 44, -55, 20]) == [-55, 17, 20, 26, 31, 44, 54, 77, 93]


def test_merge_sort_with_floats():
    """Test the merge sort on integers with neg integer."""
    assert merge_sort([54, 26.01, 93, 17, 77, 26, 44, -55, 20]) == [-55, 17, 20, 26, 26.01, 44, 54, 77, 93]


def test_selection_sort_on_integers():
    """Test the merge sort on integers."""
    assert selection_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93]


def test_selection_sort_on_words():
    """Test the selection sort on words."""
    assert selection_sort(['cat', 'dog', 'snake', 'gerbil']) == ['cat', 'dog', 'gerbil', 'snake']


def test_selection_sort_with_neg():
    """Test the selection sort on integers with neg integer."""
    assert merge_sort([54, 26, 93, 17, 77, 31, 44, -55, 20]) == [-55, 17, 20, 26, 31, 44, 54, 77, 93]


def test_selection_sort_with_floats():
    """Test the selection sort on integers with neg integer."""
    assert selection_sort([54, 26.01, 93, 17, 77, 26, 44, -55, 20]) == [-55, 17, 20, 26, 26.01, 44, 54, 77, 93]
