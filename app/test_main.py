import pytest
from app.main import get_coin_combination


def test_zero_cents():
    # Boundary condition: zero amount should return zero coins
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_single_penny():
    # Basic case: exactly 1 cent
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_single_nickel():
    # Exact value of a nickel
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_single_dime():
    # Exact value of a dime
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_single_quarter():
    # Exact value of a quarter
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_mixed_coins():
    # Testing combination of different coins
    # 17 = 1 dime (10) + 1 nickel (5) + 2 pennies (2)
    assert get_coin_combination(17) == [2, 1, 1, 0]

    # 43 = 1 quarter (25) + 1 dime (10) + 1 nickel (5) + 3 pennies (3)
    assert get_coin_combination(43) == [3, 1, 1, 1]


def test_multiple_quarters():
    # Large amount that uses multiple quarters
    # 100 = 4 quarters
    assert get_coin_combination(100) == [0, 0, 0, 4]


@pytest.mark.parametrize("cents, expected", [
    (6, [1, 1, 0, 0]),
    (11, [1, 0, 1, 0]),
    (24, [4, 0, 2, 0]),
    (99, [4, 0, 2, 3]),
])
def test_various_amounts(cents, expected):
    # Parametrized test for cleaner code and multiple coverage points
    assert get_coin_combination(cents) == expected
