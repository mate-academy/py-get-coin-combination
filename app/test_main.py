import pytest
from typing import Any
from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "coins, expected_result",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (25, [0, 0, 0, 1]),
            (27, [2, 0, 0, 1]),
            (41, [1, 1, 1, 1]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_correct_coins(self,
                           coins: int,
                           expected_result: list[int]
                           ) -> None:
        assert get_coin_combination(coins) == expected_result

    @pytest.mark.parametrize(
        "coins",
        [
            ("1"),
            ([1]),
            ({1}),
        ]
    )
    def test_raise_error_if_data_not_valid(self, coins: Any) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(coins)
