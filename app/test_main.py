import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,expected_result",
    [
        pytest.param(1, [1, 0, 0, 0], id="provided 1 coins"),
        pytest.param(6, [1, 1, 0, 0], id="provided 6 coins"),
        pytest.param(17, [2, 1, 1, 0], id="provided 17 coins"),
        pytest.param(50, [0, 0, 0, 2], id="provided 50 coins")
    ]
)
def test_get_coins(coins, expected_result):
    assert get_coin_combination(coins) == expected_result
