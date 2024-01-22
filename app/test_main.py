import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "number_of_coins, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (66, [1, 1, 1, 2]),
        (1038, [3, 0, 1, 41])
    ],
    ids=[
        "should return all zeroes if the cents is 0",
        "should return the correct amount of pennies",
        "should return the correct amount of nickels",
        "should return the correct amount of dimes",
        "should return the correct amount of quarters",
        "should return the correct amount all kinds of coins",
        "should work properly with big numbers"

    ]
)
def test_get_coin_combination_function(
        number_of_coins: int,
        result: list
) -> None:
    assert get_coin_combination(number_of_coins) == result
