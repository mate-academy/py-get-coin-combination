import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,coins",
        [
            pytest.param(
                1, [1, 0, 0, 0], id="check for penny"
            ),
            pytest.param(
                6, [1, 1, 0, 0], id="check for penny and nickel"
            ),
            pytest.param(
                17, [2, 1, 1, 0], id="check for penny, nickel and dime"
            ),
            pytest.param(
                50, [0, 0, 0, 2], id="check for quarter"
            )
        ]
    )
    def test_coin_combinations(
            self,
            cents: int,
            coins: list[int],
    ) -> None:
        assert get_coin_combination(cents) == coins
