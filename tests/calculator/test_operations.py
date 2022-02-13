from calculator.operations import (
    add,
    multiply,
    divide,
    subtract,
    )
import pytest

def test_add():
    result = add(3, 4)
    assert result == 7


def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)


def test_multiply():
    result = multiply(3, 4)
    assert result == 12

    result = multiply(0, 4)
    assert result == 0


def test_divide():
    result = divide(12, 4)
    assert result == 3


def test_subtract():
    result = subtract(12, 4)
    assert result == 8
