import pytest
from typing import List

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount,coins_list",
    [
        (4, [4, 0, 0, 0]),
        (52, [2, 0, 0, 2]),
        (41, [1, 1, 1, 1]),
        (0, [0, 0, 0, 0])
    ]
)
def test_should_calculate_num_of_coins_correctly(
        amount: int,
        coins_list: List) -> None:
    assert get_coin_combination(amount) == coins_list


def test_should_return_value_error_if_amount_is_negative_number() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)
