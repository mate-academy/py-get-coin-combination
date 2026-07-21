from app.main import get_coin_combination
import pytest


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_combination",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return 1 penny when given 1 cent"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return 1 penny and 1 nickel when given 6 cents"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should return pennies, nickel and dime for 17 cents"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should return combination of smallest number of coins"
            ),
        ]
    )
    def test_convert_to_1_penny(
            self,
            cents: int,
            expected_combination: list
    ) -> None:
        assert get_coin_combination(cents) == expected_combination
