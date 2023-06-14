import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (130, [0, 1, 0, 5]),
        (689, [4, 0, 1, 27]),
        (779, [4, 0, 0, 31]),
        (896, [1, 0, 2, 35]),
    ],
    ids=[
        "0 cents should return [0, 0, 0, 0]",
        "1 cent equals to 1 penny",
        "6 cents equal to 1 nickel + 1 penny",
        "17 cents equal to 1 dime + 1 nickel + 2 pennies",
        "50 cents equal to 2 quarters",
        "130 cents equal to 5 quarters + 1 nickel",
        "689 cents equal to 27 quarters + 1 dime + 4 pennies",
        "779 cents equal to 31 quarters + 4 pennies",
        "896 cents equal to 35 quarters + 2 dimes + 1 penny",
    ]
)
def test_get_combinations_correctly(cents: int, coins: list[int]) -> None:
    assert get_coin_combination(cents) == coins
