import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="list of zeroes if cents equal to 0"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="1 penny if cents equal to 1"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="1 penny + 1 nickel if cents equal to 6"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="2 pennies + 1 nickel + 1 dime if cents equal to 17"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="2 quarters if cents equal to 50"
        ),
    ]
)
def test_get_coin_combination(
    cents: int,
    coins: list[int],
) -> None:
    assert get_coin_combination(cents) == coins
