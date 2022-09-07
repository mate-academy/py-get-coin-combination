import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "number, expected_value",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return count of pennies"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return count of pennies and nickels"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should return count of pennies and nickels and dimes"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should return count of quarters"
            )
        ]
    )
    def test_combination_correctly(
            self,
            number,
            expected_value
    ):
        assert get_coin_combination(number) == expected_value
