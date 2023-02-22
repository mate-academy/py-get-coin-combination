import pytest
from typing import List
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected_coins", [
    pytest.param(1, [1, 0, 0, 0], id="one_penny"),
    pytest.param(6, [1, 1, 0, 0], id="one_penny_one_nickel"),
    pytest.param(17, [2, 1, 1, 0], id="two_pennies_one_nickel_one_dime"),
    pytest.param(50, [0, 0, 0, 2], id="two_quarters"),
    pytest.param(0, [0, 0, 0, 0], id="zero_cents"),
    pytest.param(1000000, [0, 0, 0, 40000], id="one_million_cents")
])
def test_get_coin_combination(cents: int, expected_coins: List[int]) -> None:
    assert get_coin_combination(cents) == expected_coins


def test_get_coin_combination_raises_error_for_negative_input() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)


def test_get_coin_combination_raises_error_for_non_integer_input() -> None:
    with pytest.raises(TypeError):
        get_coin_combination(3.5)
