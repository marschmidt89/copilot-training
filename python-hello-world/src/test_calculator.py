import pytest
from calculator import add, subtract, multiply, divide, absolute

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
    assert subtract(-5, -5) == 0

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)

def test_absolute():
    assert absolute(-10) == 10
    assert absolute(10) == 10
    assert absolute(0) == 0