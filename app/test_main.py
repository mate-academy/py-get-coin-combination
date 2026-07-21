import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,coin_combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (64, [4, 0, 1, 2]),
        (15, [0, 1, 1, 0]),
        (60, [0, 0, 1, 2]),
        (54, [4, 0, 0, 2]),
        (27, [2, 0, 0, 1]),
        (1508, [3, 1, 0, 60]),
        (13112, [2, 0, 1, 524])
    ]
)
def test_coin_combination(coins: int, coin_combination: list[int]) -> None:
    assert get_coin_combination(coins) == coin_combination, (
        f"Coin combination for {coins} cents should be {coin_combination}"
    )
