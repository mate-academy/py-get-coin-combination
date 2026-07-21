from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("coin, result", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (15, [0, 1, 1, 0]),
    (16, [1, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (26, [1, 0, 0, 1]),
    (31, [1, 1, 0, 1]),
    (41, [1, 1, 1, 1])
])
def test_each_coin_must_be_used_at_least_once(coin: int, result: list) -> None:
    goals = get_coin_combination(coin)
    assert goals == result
