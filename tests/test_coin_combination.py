import pytest
from app.coin_combination import get_coin_combination


@pytest.mark.parametrize(
    'coins,result',
    [
        [1, [1, 0, 0, 0]],
        [6, [1, 1, 0, 0]],
        [17, [2, 1, 1, 0]],
        [50, [0, 0, 0, 2]]
    ]
)
def test_different_coins(coins, result):
    assert get_coin_combination(coins) == result


def test_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]
