from app.coin_combination import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "coins, values",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (299, [4, 0, 2, 11]),

    ],
)
def test_with_different_number_of_coins(coins, values):
    assert get_coin_combination(coins) == values
