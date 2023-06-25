from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, coins",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="When cents = 0  return [0, 0, 0, 0]"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="When  cents < 5 return 1 penny = [1, 0, 0, 0]"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="When  cents > 5 return 1 penny + 1 nickel = [1, 1, 0, 0]"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="When  cents > 15 return 2 pennies + 1 nickel + 1 dime = [2, 1, 1, 0]"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="When  cents > 25 return 2 quarters = [0, 0, 0, 2]"
            )
        ]
    )
    def test_coin_combination(self,
                          cents: int,
                          coins: list[int]) -> None:
        assert get_coin_combination(cents) == coins
