import pytest
from app.main import get_coin_combination


def test_get_coin_combination_basic_cases():
    """Test basic cases from examples."""
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_get_coin_combination_zero():
    """Test with zero cents."""
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_edge_cases():
    """Test edge cases with different denominations."""
    # Only pennies
    assert get_coin_combination(4) == [4, 0, 0, 0]

    # Only nickels
    assert get_coin_combination(5) == [0, 1, 0, 0]

    # Only dimes
    assert get_coin_combination(10) == [0, 0, 1, 0]

    # Only quarters
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_get_coin_combination_mixed():
    """Test mixed combinations."""
    # 99 cents = 3 quarters + 2 dimes + 4 pennies
    assert get_coin_combination(99) == [4, 0, 2, 3]

    # 41 cents = 1 quarter + 1 dime + 1 nickel + 1 penny
    assert get_coin_combination(41) == [1, 1, 1, 1]

    # 37 cents = 1 quarter + 1 dime + 2 pennies
    assert get_coin_combination(37) == [2, 0, 1, 1]
