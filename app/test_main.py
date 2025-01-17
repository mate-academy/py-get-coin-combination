import pytest
from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_coin_combination",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="zero value"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="1 cent is 1 penny"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="6 cents are 1 penny and 1 nickel"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="17 cents are 2 pennies, 1 nickel, and 1 dime "
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="50 cents are 2 quarters"
            )
        ]
    )
    def test_correct_coin_combination(
            self,
            cents: int,
            expected_coin_combination: list
    ):
        assert get_coin_combination(cents) == expected_coin_combination
