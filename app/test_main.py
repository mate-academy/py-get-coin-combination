from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "cents,expected_coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (41, [1, 1, 1, 1])
    ],
    ids=[
        "1 cent should equal 1 penny coin",
        "6 cents should equal 1 penny + 1 nickel coin",
        "17 cents should equal 2 pennies + 1 nickel + 1 dime coin",
        "50 cents should equal 2 quarter coins",
        "41 cents should equal 1 coin of every kind"
    ]
)
def test_get_coin_combination(cents: int, expected_coins: list) -> None:
    assert get_coin_combination(cents) == expected_coins
