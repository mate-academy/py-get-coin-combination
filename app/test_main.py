import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (138, [3, 0, 1, 5]),
    ]
)
def test_get_coin_combination(coins, expected):
    assert get_coin_combination(coins) == expected
