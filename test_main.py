# Import the Add function, and assert that it works correctly.
from main import add, prod, sub

def test_add():
    assert add(2, 3) == 5

def test_prod():
    assert prod(2, 3) == 6

def test_sub():
    assert sub(3, 2) == 1
