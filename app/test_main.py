from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "coins,expected", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(coins: int, expected: list):
    assert get_coin_combination(coins) == expected
