import pytest
from app.main import get_coin_combination
from typing import List


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_coins",
        [
            pytest.param(1, [1, 0, 0, 0], id="Test pennies"),
            pytest.param
            (6, [1, 1, 0, 0], id="Test penny and nickel"),
            pytest.param
            (17, [2, 1, 1, 0], id="Test pennies, nickel and dime"),
            pytest.param
            (50, [0, 0, 0, 2], id="Test quarters"),
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            expected_coins: List[int]) -> None:
        assert get_coin_combination(cents) == expected_coins
