import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
    ids=[
        "0 cents -> zero coins",
        "1 cent -> 1 penny",
        "4 cents -> 4 pennies boundary",
        "5 cents -> 1 nickel",
        "6 cents -> 1 penny and 1 nickel",
        "9 cents -> 4 pennies and 1 nickel boundary",
        "10 cents -> 1 dime",
        "17 cents -> 2 pennies, 1 nickel, 1 dime",
        "24 cents -> 4 pennies, 2 dimes boundary",
        "25 cents -> 1 quarter",
        "50 cents -> 2 quarters",
        "99 cents -> mixed all coin types",
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
