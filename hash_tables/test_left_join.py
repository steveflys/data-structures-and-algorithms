"""Test the left join function"""

from .left_join import left_join
from .hash_table import HashTable
import pytest


def test_left_join_with_matching_keys(another_hash_table, yet_another_hash_table):
    """Test left join on hash tables with matching keys."""
    result = left_join(another_hash_table, yet_another_hash_table)
    result = sorted(result, key=lambda row: row[0])
    assert result == [['cat', 'type', 'fat'], ['dog', 'breed', 'chihuahua'], ['koala', 'temp', 'kool'], ['moose', 'cartoon', 'bullwinkle'], ['snake', 'move', None]]


def test_left_join_with_empty_left(m_t_table, yet_another_hash_table):
    """Test left_join with the left table empty."""
    assert left_join(m_t_table, yet_another_hash_table) == []


def test_left_join_with_no_matching_keys(yet_another_hash_table, final_hash_table):
    """Test left_join with no key matches."""
    result = left_join(yet_another_hash_table, final_hash_table)
    result = sorted(result, key=lambda row: row[0])
    assert result == [['cat', 'fat', None], ['dog', 'chihuahua', None], ['koala', 'kool', None], ['moose', 'bullwinkle', None]]
