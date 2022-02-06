from app.coin_combination import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "input_amount_of_cents,result_coin_combination",
    [
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (8, [3, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (84, [4, 5, 0, 3]),
    ]
)
def test_is_result_correct(input_amount_of_cents, result_coin_combination):
    assert get_coin_combination(input_amount_of_cents) == result_coin_combination
