import pytest
from app.main import get_coin_combination

@pytest.mark.parametrize("cents, expected", [
    (0,  [0, 0, 0, 0]),
    (1,  [1, 0, 0, 0]),
    (6,  [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
    (41, [1, 1, 1, 1]),
    (50, [0, 0, 0, 2]),
    (65, [0, 1, 1, 2]),
    (99, [4, 0, 2, 3])
])
def test_get_coin_combination_known(cents, expected):
    coins = get_coin_combination(cents)
    assert coins == expected
    assert isinstance(coins, list)
    assert len(coins) == 4
    assert all(isinstance(x, int) and x >= 0 for x in coins)

def test_mixed_coins_example():
    coins = get_coin_combination(17)
    assert coins[0] > 0
    assert coins[1] > 0
    assert coins[2] > 0
    assert coins[3] == 0

def test_all_coin_types():
    coins = get_coin_combination(41)
    assert all(x > 0 for x in coins)

@pytest.mark.parametrize("cents", [0, 1, 5, 10, 25, 100, 1234])
def test_format_and_total(cents):
    coins = get_coin_combination(cents)
    assert isinstance(coins, list)
    assert len(coins) == 4
    assert all(isinstance(x, int) and x >= 0 for x in coins)
    total = coins[0]*1 + coins[1]*5 + coins[2]*10 + coins[3]*25
    assert total == cents
