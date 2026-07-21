import pytest

from app.main import get_coin_combination
from typing import List


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coin, combination", [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (4, [4, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (9, [4, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (24, [4, 0, 2, 0]),
            (25, [0, 0, 0, 1])
        ]
    )
    def test_get_coin_combination(
            self,
            coin: int,
            combination: List[int]
    ) -> None:
        assert get_coin_combination(coin) == combination
