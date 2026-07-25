import pytest
from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents,coin_combination",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (6, [1, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (16, [1, 1, 1, 0]),
            (17, [2, 1, 1, 0]),
            (25, [0, 0, 0, 1]),
            (41, [1, 1, 1, 1]),
            (50, [0, 0, 0, 2]),
            (166, [1, 1, 1, 6]),
        ],
    )
    def test_different_combination_of_coin(
        self, cents: int, coin_combination: list[int]
    ) -> None:
        assert get_coin_combination(cents) == coin_combination
