from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents,coins",
        [
            pytest.param(
                1, [1, 0, 0, 0], id="test penny"
            ),
            pytest.param(
                6, [1, 1, 0, 0], id="test penny nickel"
            ),
            pytest.param(
                17, [2, 1, 1, 0], id="test penny nickel dime"
            ),
            pytest.param(
                50, [0, 0, 0, 2], id="test quarter"
            )
        ]
    )
    def test_coin_combinations(
            self,
            cents: int,
            coins: list,
    ) -> None:
        assert get_coin_combination(cents) == coins
