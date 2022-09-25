from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, coins",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="test should return zeros if count of cents is zero"
            ),
            pytest.param(
                4, [4, 0, 0, 0],
                id="test should return four pennies"
            ),
            pytest.param(
                5, [0, 1, 0, 0],
                id="test should return one nickel"
            ),
            pytest.param(
                20, [0, 0, 2, 0],
                id="test should return two dimes"
            ),
            pytest.param(
                25, [0, 0, 0, 1],
                id="test should return one quarter"
            ),
            pytest.param(
                41, [1, 1, 1, 1],
                id="test should return all coins"
            ),
            pytest.param(
                274, [4, 0, 2, 10],
                id="test should return maximum values of coins"
            )
        ]
    )
    def test_get_coin_combination(self, cents, coins):
        assert get_coin_combination(cents) == coins
