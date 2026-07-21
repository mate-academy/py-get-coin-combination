# app/test_main.py
"""
Tests for get_coin_combination.
Order of coins in the result list:
[pennies, nickels, dimes, quarters].
"""

from __future__ import annotations

from typing import List

import pytest

from app.main import get_coin_combination


COIN_VALUES: list[int] = [1, 5, 10, 25]


def _total_cents(coins: list[int]) -> int:
    """Helper: convert [p, n, d, q] to total cents."""
    return sum(count * value for count, value in zip(coins, COIN_VALUES))


@pytest.mark.parametrize(
    ("cents", "expected"),
    [
        (1, [1, 0, 0, 0]),     # 1 penny
        (6, [1, 1, 0, 0]),     # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),    # 2 pennies + 1 nickel + 1 dime
        (50, [0, 0, 0, 2]),    # 2 quarters
    ],
)
def test_examples(cents: int, expected: List[int]) -> None:
    """Matches the examples from the task."""
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents",
    [0, 4, 5, 9, 10, 24, 25, 26, 30, 41, 99],
)
def test_structure_sum_and_optimality(cents: int) -> None:
    """
    Result must:
    - be a list of 4 non-negative integers,
    - sum (in cents) to the input,
    - match the optimal greedy breakdown for US coins.
    """
    result = get_coin_combination(cents)

    # structure
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) and x >= 0 for x in result)

    # amount check
    assert _total_cents(result) == cents

    # optimal greedy oracle
    quarters = cents // 25
    rem = cents % 25
    dimes = rem // 10
    rem %= 10
    nickels = rem // 5
    pennies = rem % 5

    assert result == [pennies, nickels, dimes, quarters]


def test_zero_returns_all_zeroes() -> None:
    """Zero cents must yield zero coins of every type."""
    assert get_coin_combination(0) == [0, 0, 0, 0]
