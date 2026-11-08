import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (91, [1, 1, 1, 3]),
    ],
    ids=[
        "zero cents need no coins",
        "1 cent is one penny",
        "5 cents is one nickel",
        "6 cents is a penny and a nickel",
        "10 cents is one dime",
        "17 cents is 2 pennies, a nickel and a dime",
        "25 cents is one quarter",
        "50 cents is two quarters",
        "91 cents uses every type of coin",
    ]
)
def test_should_return_smallest_coin_combination(
        cents: int,
        coins: list
) -> None:
    assert get_coin_combination(cents) == coins
