import pytest

from app import main


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
    ],
    ids=[
        "no cents gives no coins",
        "one penny",
        "one nickel",
        "one penny and one nickel",
        "one dime",
        "2 pennies, 1 nickel and 1 dime",
        "1 nickel and 1 quarter",
        "2 quarters",
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert main.get_coin_combination(cents) == expected
