import pytest
from .stack import stack

@pytest.fixture
def small_stack():
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        