import pytest
from app.main import get_coin_combination


class TestCoin:
    @pytest.mark.parametrize(
        "cents, result",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_combination_with_minimum_coins(
            self, cents: int, result: int
    ) -> None:
        assert get_coin_combination(cents) == result
