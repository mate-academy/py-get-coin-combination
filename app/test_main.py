from app.main import get_coin_combination

import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coins,expected_combination",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return correct value if only possible "
                   "combination is in pennies"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return correct value for penny and nickel "
                   "combination"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should return correct value for penny, nickel, dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should return correct value for only quarter combo"
            )
        ]
    )
    def test_get_coin_combination(self,
                                  coins: int,
                                  expected_combination: list) -> None:
        assert get_coin_combination(coins) == expected_combination
