from typing import List

import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (99, [4, 0, 2, 3]),
            (37, [2, 0, 1, 1]),
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            expected: List[int]
    ) -> None:
        result = get_coin_combination(cents)
        assert get_coin_combination(cents) == expected, \
            f"Expected {expected} for {cents} cents, but got {result}."

    @pytest.mark.parametrize("cents", [-1, -10])
    def test_invalid_input(self, cents: int) -> None:
        assert get_coin_combination(cents) >= [0, 0, 0, 0],\
            "Coins can not be less than zero."
