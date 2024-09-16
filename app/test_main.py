import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_coins",
        [
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="test should return coins of the different types"
            ),
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="the test should return 0 of each coin type"
            )
        ]
    )
    def test_return_of_different_types_of_coins(
            self,
            cents,
            expected_coins
    ):
        assert get_coin_combination(cents) == expected_coins
