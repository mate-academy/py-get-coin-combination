from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,expexted_coins",
        [
            pytest.param(
                1, [1, 0, 0, 0],
                id="should be only 1 penny for 1 cent",
            ),
            pytest.param(
                0, [0, 0, 0, 0],
                id="should be all 0 coins for 0 cents",
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="should be 1 nickel and 1 penny for 6 cents",
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="should be 1 dime, 1 nickel and 2 pennies for 17 cents"
            ),
            pytest.param(
                50, [0, 0, 0, 2],
                id="should be only 2 quarters for 50 cents"
            ),
        ]
    )
    def test_get_coin_combination_correct(
        self,
        cents: int,
        expexted_coins: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expexted_coins
