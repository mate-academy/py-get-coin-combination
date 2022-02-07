from app.coin_combination import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "input_amount_of_cents,result_coin_combination",
    [
        pytest.param(
                    0,
                    [0, 0, 0, 0],
                    id="should return all zeroes when variable `cents` is equal to zero"
        ),
        pytest.param(
                    4,
                    [4, 0, 0, 0],
                    id="should return four and zeroes when variable `cents` is equal to four"
        ),
        pytest.param(
                    8,
                    [3, 1, 0, 0],
                    id="should return three, one, double zeroes when variable `cents` is equal to eight"
        ),
        pytest.param(
                    17,
                    [2, 1, 1, 0],
                    id="should return two, double ones, zero when variable `cents` is equal to seventeen"
        ),
        pytest.param(
                    84,
                    [4, 1, 0, 3],
                    id="should return four, five, zero, three when variable `cents` is equal to eighty-four"
        ),
    ]
)
def test_is_result_correct(input_amount_of_cents, result_coin_combination):
    assert get_coin_combination(input_amount_of_cents) == result_coin_combination
