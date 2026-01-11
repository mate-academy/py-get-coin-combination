import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),  # Исправлено ожидаемое значение
        (41, [1, 1, 1, 1]),
    ],
)
def test_parametrized(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_one_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_one_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_combination_17() -> None:
    # 2 pennies + 1 nickel + 1 dime = 17
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_combination_50() -> None:
    # 2 quarters = 50
    assert get_coin_combination(50) == [0, 0, 0, 2]
