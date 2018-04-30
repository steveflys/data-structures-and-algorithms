"""Testing for the Hash Table."""

from .hash_table import HashTable
import pytest


def test_set_and_get_on_new_hash_table():
    """Test the set and get functions on a hash_table."""
    new_hash_table = HashTable(1024)

    new_hash_table.set('potato', 24)
    assert new_hash_table.get('potato') == 24


def test_get_on_hash_table_with_bad_key():
    """Test the get function when the hash table does not contain the key."""
    new_hash_table = HashTable(1024)

    new_hash_table.set('potato', 24)
    assert new_hash_table.get('bannana') is None


def test_set_and_remove_on_new_hash_table():
    """Test the remove function."""
    new_hash_table = HashTable(1024)

    new_hash_table.set('potato', 24)
    assert new_hash_table.remove('potato') == 24

    assert new_hash_table.get('potato') is None
