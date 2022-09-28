from app.main import get_coin_combination
import pytest


class TestCoinCombination:
    @pytest.mark.parametrize("initial_variable, expected_results", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ])
    def test_values_have_the_correct_type(self, initial_variable, expected_results):
        assert get_coin_combination(initial_variable) == expected_results
