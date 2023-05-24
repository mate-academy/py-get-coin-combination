import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,combination",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "Start count from penny",
        "Checking if 1 nickel = 5 pennies",
        "Checking if 1 dime = 10 pennies",
        "Checking counting quarters"
    ]
)
def test_get_coin_combination(cents: int, combination: list) -> None:
    assert get_coin_combination(cents) == combination