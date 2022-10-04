from app.main import get_coin_combination
import pytest


class TestCoinFunc:
    @pytest.mark.parametrize(
        "coin,result", [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="test for only pennies"),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="test for pennies and nickels"),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="pennies, nickels and dimes test"),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="test only for quarters")
        ]
    )
    def test_coin_func_test(self, coin, result):

        assert get_coin_combination(coin) == result
