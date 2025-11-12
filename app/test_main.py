from typing import List

import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (66, [1, 1, 1, 2])
        ],
        ids=[
            "zero cents",
            "one penny only",
            "one penny and one nickel",
            "pennies nickel dime",
            "two quarters only",
            "all possible coins"
        ]
    )

    def test_get_coin_combination(self, cents: int, expected: List[int]) -> None:
        assert get_coin_combination(cents) == expected