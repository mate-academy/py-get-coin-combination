import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        (41, [1, 1, 1, 1]),
        (16, [1, 1, 1, 0]),
        (6, [1, 1, 0, 0]),
        (1, [1, 0, 0, 0]),
        (0, [0, 0, 0, 0]),
    ],
    ids=[
        "counts minimum coins for 41",
        "counts minimum coins for 16",
        "counts minimum coins for 6",
        "counts minimum coins for 1",
        "counts minimum coins for 0",
    ]
)
def test_get_coin_combination(cents: int, coins: list) -> None:
    assert (get_coin_combination(cents) == coins)
