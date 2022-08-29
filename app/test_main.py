import pytest

from app.main import get_coin_combination


class TestGetCoinsCombination:
    @pytest.mark.parametrize(
        "initial_number, expected_coins",
        [
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="return different coins, not only pennies"
            )
        ]
    )
    def test_count_coins_correctly(self, initial_number, expected_coins):
        assert get_coin_combination(initial_number) == expected_coins
