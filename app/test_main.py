from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, expected_coins", [
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (63, [3, 0, 1, 2]),
    (99, [4, 0, 2, 3]),
])
def test_get_coin_combination(cents: int, expected_coins: list) -> list:
    coins = get_coin_combination(cents)
    assert coins == expected_coins
