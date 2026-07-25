from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "sum_coins,coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (48, [3, 0, 2, 1])
    ]
)
def test_get_coin_combination(sum_coins: int, coins: list) -> None:
    assert (
        get_coin_combination(sum_coins) == coins
    )
