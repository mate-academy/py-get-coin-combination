import pytest
from typing import Any
from app import main


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_coins",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (69, [4, 1, 1, 2]),
            (50, [0, 0, 0, 2]),
            (10000, [0, 0, 0, 400]),
            (-1, [4, 0, 2, -1])
        ],
        ids=[
            "0 cents",
            "1 penny",
            "1 penny + 1 nickel",
            "2 pennies + 1 nickel + 1 dime",
            "4 pennies + 1 nickel + 1 dime + 2 quarters",
            "2 quarters",
            "400 quarters",
            "negative input returns invalid combination"
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            expected_coins: list[int]
    ) -> None:
        assert (
            main.get_coin_combination(cents) == expected_coins
        ), f" {cents} cents should be {expected_coins} in coins"

    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            pytest.param(
                "10",
                TypeError,
                id="Value cannot not be string"
            ),
            pytest.param(
                None,
                TypeError,
                id="Value cannot be None"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            cents: Any,
            expected_error: type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            main.get_coin_combination(cents)
