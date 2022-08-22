from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "denomination,expected_value",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_should_return_the_least_number_of_coins(self, denomination, expected_value):
        result = get_coin_combination(denomination)
        assert result == expected_value
