"""Test the repeated word function."""

import pytest
from .repeated_word import repeated_word


def test_repeated_word_on_moby_dick():
    """Use the first paragraph of Moby Dick to test the repeated_word function."""
    moby_dick = 'Call me Ishmael. Some years ago- never mind how long precisely- having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people\'s hats off- then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.'

    assert repeated_word(moby_dick) == 'me'


def test_repeated_word_with_no_repeated_words():
    """Test the repeated_word function when there is no repeated word."""
    testing = 'Write at least three test assertions for each method that you define.'

    assert repeated_word(testing) is False


def test_repeated_word_with_numbers_and_no_repeated_words():
    """Test the repeated_wrod function with a paragraph with numbers."""
    testing = 'Write at least 3 test assertions for every 1 method that you define.'

    assert repeated_word(testing) is False
