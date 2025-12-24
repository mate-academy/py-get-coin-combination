import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coin_combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (167, [2, 1, 1, 6])
    ],
    ids=[
        "test zeros values",
        "test right combination for 1 penny",
        "test right combination for 1 nickel",
        "test right combination for 1 dime",
        "test right combination for 1 quarter",
        "test right combination for all coin",
        "test right combination for big value",
    ]
)
def test_coin_combination(cents: int, coin_combination: list) -> None:
    assert get_coin_combination(cents) == coin_combination
