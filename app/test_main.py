from app.main import get_coin_combination
import pytest


class TestCoinsNeeded:
    @pytest.mark.parametrize(
        "cents,expected_coins",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="test no money 😢"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="test 1 penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="test 1 penny + 1 nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="test 2 pennies + 1 nickel + 1 dime"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="test 2 quarters"
            ),
            pytest.param(
                66,
                [1, 1, 1, 2],
                id="test all types of values needed"
            ),
            pytest.param(
                999,
                [4, 0, 2, 39],
                id="test just curious"
            ),
        ]
    )
    def test_get_coin_combination(self,
                                  cents: int,
                                  expected_coins: list[int]
                                  ) -> None:
        assert get_coin_combination(cents) == expected_coins
