import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "count_of_cents, coin_combination",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="Test should return 1 penny"
            ),
            pytest.param(
                18,
                [3, 1, 1, 0],
                id="Test should return 3 pennies 1 nickel 1 dime"
            ),
            pytest.param(
                7,
                [2, 1, 0, 0],
                id="Test should return 2 pennies 1 nickel"
            ),
            pytest.param(
                20,
                [0, 0, 2, 0],
                id="Test should return 2 dimes"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="Test should return 2 quarters"
            ),
            pytest.param(
                739,
                [4, 0, 1, 29],
                id="Test should return correct combination for "
                   "big number of cents"
            )
        ]
    )
    def test_coin_combinations(
            self,
            count_of_cents,
            coin_combination
    ):
        assert get_coin_combination(count_of_cents) == coin_combination
