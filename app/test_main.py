import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1])
    ],
    ids=[
        "returns penny",
        "returns nickel",
        "returns dime",
        "returns quarter",
        "returns every coin"
    ]
)
def test_get_coin_combination(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins
