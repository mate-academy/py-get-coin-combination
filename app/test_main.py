import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "initial_cents,expected_combination_of_coins",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
        ],

    )
    def test_get_coin_combination_validation(self,
                                             initial_cents,
                                             expected_combination_of_coins):
        result = get_coin_combination(initial_cents)
        assert result == expected_combination_of_coins
