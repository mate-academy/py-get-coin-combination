import pytest
from app.coin_combination import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_coin_combination",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return zeroes when `cents` equal to zero",
        ),
        pytest.param(
            2,
            [2, 0, 0, 0],
            id="should return correct combination of pence",
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return correct combination of pence and nickels",
        ),
        pytest.param(
            18,
            [3, 1, 1, 0],
            id="should return correct combination of pence, nickels and dimes"
        ),
        pytest.param(
            72,
            [2, 0, 2, 2],
            id="should return correct combination of all coins together"
        ),
    ]
)
def test_coin_combination_is_correct(cents, expected_coin_combination):
    assert get_coin_combination(cents) == expected_coin_combination
