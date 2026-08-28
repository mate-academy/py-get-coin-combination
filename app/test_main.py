from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "coins,expected",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (4, [4, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_calculations_coins_correctly(
            self,
            coins: int,
            expected: list[int]
    ) -> None:
        assert get_coin_combination(coins) == expected
