from .multi_bracket_validation import multi_bracket_validation
from .multi_bracket_validation import switch
import pytest


def test_switch():
    """test the switch will reverse the bracket characters"""
    assert switch('(') == ')'
    assert switch('[') == ']'
    assert switch('{') == '}'


def test_multi_bracket_validation():
    """test that we can push validate different string situations"""
    # assert multi_bracket_validation('help([me])') is True
    assert multi_bracket_validation('{}[()]') is True
    assert multi_bracket_validation('[n*&](\})') is False
    assert multi_bracket_validation('what is(2+2)[()') is False
