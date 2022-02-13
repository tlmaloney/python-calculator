from calculator.operations import add, multiply
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
    assert result == 1 # make it fail
