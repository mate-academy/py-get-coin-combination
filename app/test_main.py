import pytest

from app.main import get_coin_combination

@pytest.mark.parametrize(
    "cents,coins",
    [
        pytest.param(24, [4, 0, 2, 0], id="small amount"),
        pytest.param(1024, [4, 0, 2, 40], id="large amount"),
        pytest.param(117, [2, 1, 1, 4], id="all coin types"),
        pytest.param(1, [1, 0, 0, 0], id="single coin"),
        pytest.param(0, [0, 0, 0, 0], id="zero cents")
    ]
)
def test_different_amounts_and_coin_combinations(cents, coins) -> None:
    assert get_coin_combination(cents) == coins


def test_sum_of_coins_equals_cents() -> None:
    values = [1, 5, 10, 25]
    sum_of_coins = 0
    result = get_coin_combination(117)
    for i in range(len(values)):
        sum_of_coins += result[i] * values[i]
    assert sum_of_coins == 117

