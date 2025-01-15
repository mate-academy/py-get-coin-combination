import pytest
from app.main import get_coin_combination


def test_return_only_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_return_penny_and_nickel():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_return_pennies_nickel_dime():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_return_quarters():
    assert get_coin_combination(50) == [0, 0, 0, 2]


@pytest.mark.parametrize(
    "cents, expected", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_various_cases(cents, expected) -> None:
    assert get_coin_combination(cents) == expected
