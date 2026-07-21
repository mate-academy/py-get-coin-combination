import pytest
from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_coins",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (30, [0, 1, 0, 1]),
            (41, [1, 1, 1, 1]),
            (99, [4, 0, 2, 3]),
            (123, [3, 0, 2, 4]),
            (50, [0, 0, 0, 2]),
        ]
    )
    def test_get_coin_combination(self,
                                  cents: int,
                                  expected_coins: int) -> None:
        assert get_coin_combination(cents) == expected_coins
