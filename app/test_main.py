import pytest
from _pytest.mark import ParameterSet

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "input_date, result",
        [
            pytest.param(66, [1, 1, 1, 2], id="should use all coins"),
            pytest.param(17, [2, 1, 1, 0], id="should use 2 penalty coins"),
            pytest.param(20, [0, 0, 2, 0], id="should use only 2 dime coins"),

        ]

    )
    def test_should_check_return_different_coins(
        self,
        input_date: ParameterSet,
        result: ParameterSet
    ) -> None:
        assert get_coin_combination(input_date) == result
