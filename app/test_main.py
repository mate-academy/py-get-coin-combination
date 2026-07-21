import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_coins",
        [
            pytest.param(
                0, [0, 0, 0, 0],
                id="should return list of zeros when input is 0"),
            pytest.param(
                1, [1, 0, 0, 0],
                id="should return 1 penny when input is 1"),
            pytest.param(
                6, [1, 1, 0, 0],
                id="should return 1 penny + 1 nickel when input is 6"),
            pytest.param(
                17, [2, 1, 1, 0],
                id="should return 2 pennies + 1 nickel +"
                   " 1 dime when input is 17"),
            pytest.param(
                50, [0, 0, 0, 2],
                id="should return 2 quarters when input is 50"),
            pytest.param(
                3342, [2, 1, 1, 133],
                id="should work correctly with big values")
        ]
    )
    def test_get_coin_combination_correctly(
            self,
            cents: int,
            expected_coins: list
    ) -> None:
        assert get_coin_combination(cents) == expected_coins
