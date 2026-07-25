import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (42, [2, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
    ],
    ids=[
        "should return zeros for 0 pennies",
        "should return only pennies for value < 5 cents",
        "should return only nickel for value % 5 == 0 cents",
        "should return pennies and nickels for value > 5 cents and  % 10 == 0",
        "should return only dimes for value % 10 cents",
        "should return pennies, nickels and dimes for value >= 16 and < 41",
        "should return pennies, nickels, dimes and quarters for value > 41",
        "should return only quarters for value % 25 == 0",
    ]
)
def test_get_coin_combination_correctly(
        cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(cents) == expected_result
