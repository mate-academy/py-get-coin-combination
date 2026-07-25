import pytest
from app.main import get_coin_combination


def test_get_number_of_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_numbers_of_nickels() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_number_of_dimes() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_number_of_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_coins_combination(cents: int, expected: [int, int, int, int]) -> None:
    assert get_coin_combination(cents) == expected
