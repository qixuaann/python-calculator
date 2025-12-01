import pytest
from calculator import add, power, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_add(a, b, expected):
    """Test addition function."""
    assert add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [(5, 3, 2), (0, 5, -5), (-3, -2, -1)])
def test_subtract(a, b, expected):
    """Test subtraction function."""
    assert subtract(a, b) == expected

def test_multiply():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    """Test division function."""
    assert divide(8, 2) == 4
    assert divide(9, 3) == 3
    assert divide(-10, 2) == -5

@pytest.mark.edge
def test_divide_by_zero():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.slow
def test_power():
    """Test power function."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 2) == 9