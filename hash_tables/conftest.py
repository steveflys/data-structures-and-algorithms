"""Test fixtures for the pytests on the HashList class."""

import pytest
from .hash_table import HashTable


@pytest.fixture
def repeat_key_hash_table():
    """Make a hash table with multiple values with the same key."""
    h = HashTable()
    h.set('dog', 1)
    h.set('dog', 2)
    h.set('dog', 3)
    return h


@pytest.fixture
def different_key_hash_table():
    """Make a hash table with multiple values and keys."""
    h = HashTable()
    h.set('dog', 1)
    h.set('cat', 2)
    h.set('moose', 3)
    return h
