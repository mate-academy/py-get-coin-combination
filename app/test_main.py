from app.main import get_coin_combination

import pytest


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents, expected_combination",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (20, [0, 0, 2, 0]),
            (50, [0, 0, 0, 2]),
            (66, [1, 1, 1, 2]),
        ],
        ids=[
            "incoming_data is zero",
            "in combination only penny",
            "in combination penny and nickel",
            "in combination pennies and nickel and dime",
            "in combination only dime",
            "in combination only quarters",
            "in combination all coins",
        ]
    )
    def test_correct_incoming_data(
            self,
            cents: int,
            expected_combination: list[int]) -> None:
        assert get_coin_combination(cents) == expected_combination
