import pytest
from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected",
        [
            pytest.param(
                1, [1, 0, 0, 0],
                id="1 penny"
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="1 penny + 1 nickel"
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="2 pennies + 1 nickel + 1 dime"
            ),
            pytest.param(
                50, [0, 0, 0, 2],
                id="2 quarters"
            ),
            pytest.param(
                0, [0, 0, 0, 0],
                id="0 cents"
            ),
            pytest.param(
                99, [4, 0, 2, 3],
                id="99 cents = 4 pennies + 2 dimes + 3 quarters"
            ),
            pytest.param(
                25, [0, 0, 0, 1],
                id="1 quarter"
            ),
            pytest.param(
                41, [1, 1, 1, 1],
                id="1 penny + 1 nickel + 1 dime + 1 quarter"
            ),
        ]
    )
    def test_get_coin_combination(self,
                                  cents: int,
                                  expected: list) -> None:
        assert get_coin_combination(cents) == expected
