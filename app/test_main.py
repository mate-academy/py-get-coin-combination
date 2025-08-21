import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,result",
    [
        (4, [4, 0, 0, 0]),
        (9, [4, 1, 0, 0]),
        (21, [1, 0, 2, 0]),
        (30, [0, 1, 0, 1]),
    ]
)
def test_coins(coins: int, result: list[int]) -> None:
    assert (get_coin_combination(coins) == result)

