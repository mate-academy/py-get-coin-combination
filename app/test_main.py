import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_coin_combination",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
    ids=[
        "1 cent should return 1 penny",
        "6 cents should return a combination of 1 penny + 2 nickel",
        "17 cents should return a combination of 2 pennies + 1 nickel + 1 dime",
        "50 cents should return a combination of 2 quarters",
    ]
)
def test_get_coin_combination(cents: int, expected_coin_combination) -> None:
    assert get_coin_combination(cents) == expected_coin_combination
