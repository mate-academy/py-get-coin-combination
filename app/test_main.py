import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (16, [1, 1, 1, 0]),
        (41, [1, 1, 1, 1])
    ],
    ids=[
        "penny",
        "penny + nickel",
        "penny + nickel+dime",
        "penny + nickel+dime+quarter"
    ]
)
def test_get_coin_combination(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins
