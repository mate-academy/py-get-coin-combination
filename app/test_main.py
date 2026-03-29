import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="Function should return list of zeroes if cents = 0"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="Function should return one penny if cents = 1"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="Function should return 1 penny + 1 nickel if cents = 6"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="Function should return 2 pennies "
               "+ 1 nickel + 1 dime if cents = 17"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="Function should return 2 quarters if cents = 50,"
        ),
    ]
)
def test_get_coin_combination(
    cents: int,
    coins: list[int],
) -> None:
    assert get_coin_combination(cents) == coins
