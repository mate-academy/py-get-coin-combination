from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "coins,result",
    [
        (1, [1, 0, 0, 0]),
        (0, [0, 0, 0, 0]),
        (74, [4, 0, 2, 2]),
        (900980, [0, 1, 0, 36039])
    ]
)
def test_get_coin_combination(coins: int, result: list) -> None:
    assert get_coin_combination(coins) == result
