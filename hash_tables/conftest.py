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


@pytest.fixture
def m_t_table():
    """Make a hash table with multiple values and keys."""
    h = HashTable()
    return h


@pytest.fixture
def another_hash_table():
    """Make a hash table with multiple values and keys."""
    h = HashTable()
    h.set('dog', 'breed')
    h.set('cat', 'type')
    h.set('moose', 'cartoon')
    h.set('koala', 'temp')
    h.set('snake', 'move')
    return h


@pytest.fixture
def yet_another_hash_table():
    """Make a hash table with multiple values and keys."""
    h = HashTable()
    h.set('koala', 'kool')
    h.set('dog', 'chihuahua')
    h.set('cat', 'fat')
    h.set('moose', 'bullwinkle')
    return h


@pytest.fixture
def final_hash_table():
    """Make a hash table with multiple values and keys."""
    h = HashTable()
    h.set('22', 'kool')
    h.set('42', 'chihuahua')
    h.set('666', 'fat')
    h.set('rocky', 'bullwinkle')
    return h
