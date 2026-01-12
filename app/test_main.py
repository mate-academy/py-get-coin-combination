import pytest
from typing import Any
from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, result_list",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (41, [1, 1, 1, 1]),
            (50, [0, 0, 0, 2]),
            (101, [1, 0, 0, 4]),
            (1016, [1, 1, 1, 40]),
        ]
    )
    def test_get_coin_combination(self,
                                  cents: int,
                                  result_list: list[int]) -> None:
        assert get_coin_combination(cents) == result_list

    @pytest.mark.parametrize(
        "wrong_type",
        [
            "Some string",
            None,
            [0, 0],
            {0: 0},
            {0, 0}
        ]
    )
    def test_wrong_type_get_coin_combination(self, wrong_type: Any) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(wrong_type)
