from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4])
    ]
)
def test_combination_coin(cents: int, result: list) -> None:
    coin_get = get_coin_combination(cents)
    assert coin_get == result
    assert isinstance(coin_get, list)
    assert all(isinstance(i, int) for i in coin_get)
