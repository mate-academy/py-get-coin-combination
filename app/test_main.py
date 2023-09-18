import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("coins, expected_result",[
                             (1, [1, 0, 0, 0]),
                             (6, [1, 1, 0, 0]),
                             (17, [2, 1, 1, 0]),
                             (50, [0, 0, 0, 2]),
    (1000000, [0, 0, 0, 40000]),

])
def test_check_coins_combination_coin_has_dif_amount(coins, expected_result) -> None:
    assert get_coin_combination(coins) == expected_result

def test_check_type_return_list() -> None:
    result = get_coin_combination(cents=100)
    assert isinstance(result, list)

