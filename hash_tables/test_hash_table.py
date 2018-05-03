"""Testing for the Hash Table."""

from .hash_table import HashTable
import pytest


def test_set_and_get_on_new_hash_table():
    """Test the set and get functions on a hash_table."""
    new_hash_table = HashTable()
    new_hash_table.set('potato', 24)
    assert new_hash_table.get('potato') == [24]


def test_get_on_a_key_with_multiple_values(repeat_key_hash_table):
    assert repeat_key_hash_table.get('dog') == [3, 2, 1]


def test_key_is_not_a_string():
    """Test TypeError is returned when the key is not a string."""
    new_hash_table = HashTable()
    with pytest.raises(TypeError):
        new_hash_table.set(17,24)
    #  assert new_hash_table.set(17, 24) is TypeError


def test_get_on_hash_table_with_bad_key():
    """Test the get function when the hash table does not contain the key."""
    new_hash_table = HashTable()
    new_hash_table.set('potato', 24)
    assert new_hash_table.get('bannana') is None


def test_remove_on_new_hash_table(repeat_key_hash_table):
    """Test the remove function."""
    assert repeat_key_hash_table.remove('dog') == [3, 2, 1]


def test_remove_actually_removes_nodes():
    """Test the remove function."""
    test_table = HashTable()
    test_table.set('dog', 1)
    test_table.set('dog', 2)
    test_table.set('dog', 3)
    test_table.remove('dog')
    assert test_table.get('dog') == []
