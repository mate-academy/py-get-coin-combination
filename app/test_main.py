import pytest
from app.main import get_coin_combination


def test_get_coin_combination_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


@pytest.mark.parametrize("cents, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (30, [0, 1, 0, 1]),
    (99, [4, 0, 2, 3]),
])
def test_get_coin_combination_parametrized(
        cents: int, expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected
