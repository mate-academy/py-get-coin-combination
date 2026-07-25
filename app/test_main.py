from typing import Type

import pytest
from app.main import get_coin_combination


class TestGetCoinCombinations:
    @pytest.mark.parametrize(
        "cents,coins",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (0, [0, 0, 0, 0]),
        ],
        ids=[
            "Should return 1 penny.",
            "Should return 1 penny + 1 nickel.",
            "Should return 2 pennies + 1 nickel + 1 dime.",
            "Should return 2 quarters.",
            "Should return list of zeros if cents is zero.",
        ]
    )
    def test_return_coins(
            self, cents: int, coins: list[int]
    ) -> None:
        assert get_coin_combination(cents) == coins

    @pytest.mark.parametrize(
        "cents,expected_exception",
        [
            ([1], TypeError),
        ],
        ids=[
            "Should except TypeError if cents is not integer",
        ]
    )
    def test_should_except_correct_exception(
            self,
            cents: int,
            expected_exception: Type[Exception]
    ) -> None:
        with pytest.raises(expected_exception):
            get_coin_combination(cents)
