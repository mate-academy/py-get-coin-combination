from app.main import get_coin_combination
from typing import List
import pytest


class TestGetCoins:
    @pytest.mark.parametrize("coins,expected", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
    ])
    def test_get_correct_results(
            self,
            coins: int,
            expected: List[int]
    ) -> Exception | None:
        assert get_coin_combination(coins) == expected
