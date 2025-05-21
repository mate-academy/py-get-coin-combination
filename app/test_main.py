# rer8
import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, result_list",
    [
        pytest.param(1, [1, 0, 0, 0],
                     id="when_have_1_coin_then_return_1_penny"),
        pytest.param(6, [1, 1, 0, 0],
                     id="6_coin_then_return_1_penny_1_nickel"),
        pytest.param(10, [0, 0, 1, 0],
                     id="10_coin_then_return_1_dime"),
        pytest.param(15, [0, 1, 1, 0],
                     id="15_coin_then_return_1_nickel_1_dime"),
        pytest.param(17, [2, 1, 1, 0],
                     id="17_coin_then_return_2_penny_1_nickel_1_dime"),
        pytest.param(20, [0, 0, 2, 0],
                     id="20_coin_then_return_2_dime"),
        pytest.param(22, [2, 0, 2, 0],
                     id="22_coin_then_return_2_penny_2_dime"),
        pytest.param(23, [3, 0, 2, 0],
                     id="23_coin_then_return_3_penny_2_dime"),
        pytest.param(50, [0, 0, 0, 2],
                     id="50_coin_then_return_2_quarter")
    ])
def test_get_coin_combination(coins: int, result_list: list[int]) -> None:
    result = get_coin_combination(coins)
    assert result == result_list
