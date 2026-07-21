import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ],
        ids=[
            "1 penny",
            "1 penny + 1 nickel",
            "2 pennies + 1 nickel + 1 dime",
            "2 quarters"
        ]
    )
    def tests_for_correct_coins_combinations(
            self,
            cents: int,
            expected_result: list
    ) -> None:
        assert get_coin_combination(cents) == expected_result
