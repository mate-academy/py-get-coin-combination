import pytest
from typing import Type, Any

from app.main import get_coin_combination


valid_cases = [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (2, [2, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (15, [0, 1, 1, 0]),
    (35, [0, 0, 1, 1]),
    (40, [0, 1, 1, 1]),
    (41, [1, 1, 1, 1]),
    (100, [0, 0, 0, 4]),
    (153, [3, 0, 0, 6]),
    (116, [1, 1, 1, 4]),
    (74, [4, 0, 2, 2])
]


@pytest.mark.parametrize(
    "cents,coins",
    valid_cases,
    ids=[f"{c} cents -> {coins}" for c, coins in valid_cases]
)
def test_get_coin_combination_returns_correct_result(
        cents: int,
        coins: list[int]
) -> None:
    assert get_coin_combination(cents) == coins


invalid_cases = [
    (-5, ValueError),
    (-1, ValueError),
    ("5", TypeError),
    (1.5, TypeError),
    (True, TypeError),
    ((1, 2, 3, 4), TypeError)
]


@pytest.mark.parametrize(
    "cents,expected_error",
    invalid_cases,
    ids=[f"{c} cents -> {error.__name__}" for c, error in invalid_cases]
)
def test_get_coin_combination_raises_error_when_not_valid_cents(
        cents: Any,
        expected_error: Type[BaseException]
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)
