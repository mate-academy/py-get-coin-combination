from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, coins", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (2, [2, 0, 0, 0]),
    (3, [3, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (18, [3, 1, 1, 0]),
    (21, [1, 0, 2, 0]),
    (25, [0, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (50, [0, 0, 0, 2]),
    (51, [1, 0, 0, 2]),
])
def test_get_coin_combination(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins
