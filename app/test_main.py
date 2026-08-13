import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, values",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "1 coin",
        "6 coins",
        "17 coins",
        "50 coins"
    ]
)
def test_coin_combination(coins: int, values: list[int]) -> None:
    assert get_coin_combination(coins) == values
