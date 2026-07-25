import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,pennies,nickels,dimes,quarters",
        [
            pytest.param(
                0, 0, 0, 0, 0, id="tests all coins are zeroes"
            ),
            pytest.param(
                3, 3, 0, 0, 0, id="tests only pennies"
            ),
            pytest.param(
                7, 2, 1, 0, 0, id="tests pennies and nickels"
            ),
            pytest.param(
                19, 4, 1, 1, 0, id="tests pennies, nickels and dimes"
            ),
            pytest.param(
                194, 4, 1, 1, 7, id="tests all coins"
            )
        ]
    )
    def test_min_combination(
            self,
            cents: int,
            pennies: int,
            nickels: int,
            dimes: int,
            quarters: int
    ) -> None:
        assert get_coin_combination(cents) == [
            pennies, nickels, dimes, quarters
        ]
