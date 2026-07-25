import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "1 penny should equal 1 penny",
        "6 pennies should equal 1 penny + one nickel",
        "17 pennies should equal 2 pennies + 1 nickel + 1 dime",
        "50 pennies should equal 2 quarters"
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected
