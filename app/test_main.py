import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (16, [1, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
    ],
    ids=[
        "0 cents should convert to 0 coins",
        "1 cent should convert to 1 penny coin",
        "6 cents should convert to 1 penny and 1 nickel coin",
        "16 cents should convert to 1 penny, 1 nickel, 1 dime coin",
        "41 cents should convert to 1 penny, 1 nickel, 1 dime, 1 quarter coin",
    ]
)
def test_coin_combination(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins
