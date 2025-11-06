import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (41, [1, 1, 1, 1]),
    (49, [4, 0, 2, 1]),
    (50, [0, 0, 0, 2]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4]),
    (123, [3, 0, 2, 4]),
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_only_pennies() -> None:
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_only_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_only_dimes() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_only_quarters() -> None:
    assert get_coin_combination(75) == [0, 0, 0, 3]


def test_combination_of_all_coin_types() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]
