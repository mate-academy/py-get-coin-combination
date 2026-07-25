"""Tests for get_coin_combination function."""

import pytest
from app.main import get_coin_combination


def test_one_cent() -> None:
    """Should return 1 penny for 1 cent."""
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_six_cents() -> None:
    """Should return 1 penny and 1 nickel for 6 cents."""
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_seventeen_cents() -> None:
    """Should return 2 pennies, 1 nickel, and 1 dime for 17 cents."""
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_fifty_cents() -> None:
    """Should return 2 quarters for 50 cents."""
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_only_dimes() -> None:
    """Should return 3 dimes for 30 cents."""
    assert get_coin_combination(30) == [0, 0, 3, 0]


def test_only_nickels() -> None:
    """Should return 4 nickels for 20 cents."""
    assert get_coin_combination(20) == [0, 4, 0, 0]


def test_zero_cents() -> None:
    """Should return all zeros for 0 cents."""
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_large_amount() -> None:
    """Should return minimal coins for 99 cents."""
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_negative_input() -> None:
    """Should raise ValueError for negative input."""
    with pytest.raises(ValueError):
        get_coin_combination(-5)
