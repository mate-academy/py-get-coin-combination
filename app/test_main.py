import pytest

from app.main import get_coin_combination


class TestCoinCombinations:
    @pytest.mark.parametrize(
        "coins_amount,expected_list",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should return a list with zeros, when amount of coins is 0"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return a list with one penny => [1, 0, 0, 0]"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return a list with 1 penny and 1 nickel => "
                   "[1, 1, 0, 0]"
            ),
            pytest.param(
                16,
                [1, 1, 1, 0],
                id="should return a list with 1 penny, 1 nickel and 1 dime => "
                   "[1, 1, 1, 0]"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="should return a list with 1 penny, 1 nickel, 1 dime and "
                   "quarter => [1, 1, 1, 1]"
            ),
            pytest.param(
                97,
                [2, 0, 2, 3],
                id="should return a list with various combination of coins "
                   "=> [2, 0, 2, 3]"
            )
        ]
    )
    def test_coins_combinations(
            self,
            coins_amount: int,
            expected_list: list
    ) -> None:
        assert get_coin_combination(coins_amount) == expected_list
