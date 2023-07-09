from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, expected_coins", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
    (0, [0, 0, 0, 0]),
    (99, [4, 0, 2, 3]),
    (82, [2, 1, 0, 3]),
])
def test_get_coin_combination(cents: int, expected_coins: list) -> None:
    coins = get_coin_combination(cents)
    assert coins == expected_coins
