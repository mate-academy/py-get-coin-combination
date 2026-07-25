import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("cents, coins", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2])
])
def test_right_combination_coins(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins
