import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected",
[
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (24, [4, 0, 2, 0]),
    (49, [4, 0, 2, 1]),
    (99, [4, 0, 2, 3]),
],

ids=
[
    "1 cent = 1 penny",
    "6 cents = 1 penny + 1 nickel",
    "17 cents = 2 pennies + 1 nickel + 1 dime",
    "50 cents = 2 quarters",
    "5 cents = 1 nickel",
    "10 cents = 1 dime",
    "25 cents = 1 quarter",
    "24 cents = 4 pennies + 2 dimes",
    "49 cents = 4 pennies + 2 dimes + 1 quarter",
     "99 cents = 3 quarters + 2 dimes + 4 pennies"
])


def test_get_coin_combination(cents: int,
                              expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected, \
        (f"Expected {expected} for {cents} cents, "
         f"but got {get_coin_combination(cents)}")


@pytest.mark.parametrize("cents, expected",
[
    (0, [0, 0, 0, 0]),
    (-1, [0, 0, 0, 0]),
],
ids=
[
    "0 cents = no coins",
    "-1 cents = no coins",
])


def test_get_coin_combination_boundaries(cents: int,
                                         expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected, \
        (f"Expected {expected} for {cents} cents,"
         f" but got {get_coin_combination(cents)}")

if __name__ == "__main__":
    pass
