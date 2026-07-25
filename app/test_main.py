from typing import Any

import pytest

from app.main import get_coin_combination


# write your tests here
class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coins, correct_answer",
        [
            pytest.param(1, [1, 0, 0, 0], id="1 must return [1, 0, 0, 0]"),
            pytest.param(6, [1, 1, 0, 0], id="6 must return [1, 1, 0, 0]"),
            pytest.param(17, [2, 1, 1, 0], id="1 must return [2, 1, 1, 0]"),
            pytest.param(50, [0, 0, 0, 2], id="50 must return [0, 0, 0, 2]")
        ]
    )
    def test_get_coin_combination_with_correct_parameters(
            self,
            coins: int,
            correct_answer: list[int]
    ) -> None:
        assert get_coin_combination(coins) == correct_answer

    @pytest.mark.parametrize(
        "incorrect_param",
        [
            pytest.param("1", id="not integer value must raise TypeError"),
            pytest.param(["1"], id="not integer value must raise TypeError")
        ]
    )
    def test_get_coin_combination_with_incorrect_parameters(
            self,
            incorrect_param: Any
    ) -> None:
        with pytest.raises(TypeError):
            assert get_coin_combination(incorrect_param)
